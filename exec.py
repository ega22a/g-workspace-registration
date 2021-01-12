# Импорт системных библиотек
from __future__ import print_function
from shutil import copyfile
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from PyQt5 import QtWidgets, QtCore
import sys, smtplib, json, ssl, random, string, webbrowser, csv
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from email.header import Header
from string import Template
# Импорт форм
from form_mainForm import Ui_mainForm
from form_dialogJSONCreds import Ui_formJSONCreds
from form_emailSettings import Ui_form_emailSettings
from form_checkEmail import Ui_form_checkEmail
from form_editUser import Ui_form_editUser
from form_regUser import Ui_form_regUser

# Инициализация констант
SCOPES = [
    'https://www.googleapis.com/auth/admin.directory.user',
    'https://www.googleapis.com/auth/admin.directory.orgunit'
    ]
CREDENTIALS = 'credentials.json'
SETTINGS = 'settings.json'
DIRECTORY_API = None
PAYLOAD = {
    'orgUnits': None,
    'settings': None
}
EDITABLE_ID = None
application = None
_dialogJSON = None
_emailSettings = None
_checkEmail = None
_dialogEditUser = None
_dialogRegUser = None

# Функция получения полного пути до файла
getFullPath = lambda _path = '': os.path.join(os.path.dirname(__file__), _path)

# Функция генерации случайной строки
getRandomString = lambda _length = 8: ''.join(random.choice(string.ascii_letters) for i in range(_length))

# Функция создания окна подтверждения с последующим возвращением булевого ответа
confirm = lambda _header = 'HEADER_IS_NOT_SET', _message = 'MESSAGE_IS_NOT_SET': QtWidgets.QMessageBox.question(None, _header, _message, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No) == QtWidgets.QMessageBox.Yes

# Процедура создания окна предупреждения
def alert(_header:str = 'HEADER_IS_NOT_SET', _message:str = 'MESSAGE_IS_NOT_SET', _type:str = 'information'):
    if _type == 'information':
        QtWidgets.QMessageBox.information(None, _header, _message, QtWidgets.QMessageBox.Ok)
    elif _type == 'warning':
        QtWidgets.QMessageBox.warning(None, _header, _message, QtWidgets.QMessageBox.Ok)
    elif _type == 'critical':
        QtWidgets.QMessageBox.critical(None, _header, _message, QtWidgets.QMessageBox.Ok)

# Рекурсивная функция создания организационных подразделений
def collectOrgUnits(_orgUnits = None, _qTree = None):
    _returned = []
    for orgUnit in _orgUnits:
        _secReturn = {
            'name': orgUnit['name'],
            'orgUnitId': orgUnit['orgUnitId'],
            'orgUnitPath': orgUnit['orgUnitPath'],
            'in': None
        }
        _newTree = QtWidgets.QTreeWidgetItem(_qTree)
        _newTree.setText(0, orgUnit['name'])
        _check = DIRECTORY_API.orgunits().list(customerId='my_customer', orgUnitPath=orgUnit.get('orgUnitPath')).execute()
        if _check.get('organizationUnits'):
            _secReturn.update({'in': collectOrgUnits(_orgUnits = _check.get('organizationUnits'), _qTree = _newTree)})
        _returned.append(_secReturn)
    return _returned

# Функция проверки существования файла (относительные пути)
checkFileExsist = lambda _file: os.path.isfile(getFullPath(_file))

# Инициализация подключения к Directory API (Google Workspace)
def directoryAPI_exec():
    if (checkFileExsist(CREDENTIALS)):
        creds = None
        if os.path.exists('rick.pickle'):
            with open('rick.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS, SCOPES)
                creds = flow.run_local_server(port=0)
            with open('rick.pickle', 'wb') as token:
                pickle.dump(creds, token)
        return build('admin', 'directory_v1', credentials=creds)
    else:
        return False

# Функция подстановки текста в шаблоны
def getFormattedText(_filename:str = None, _args:dict = None):
    if (_filename != None):
        with open(_filename, 'r') as _f:
            return _f.read() if _args == None else Template(_f.read()).substitute(_args)
    else:
        return False

# Функция отправки писем через TLS SMTP
def sendMail(_payloads:list = None):
    if (PAYLOAD.get('settings') != None) & (_payloads != None):
        _emailSettings = PAYLOAD['settings']['email']
        try:
            _server = smtplib.SMTP_SSL(_email['address'], int(_email['port']))
            _server.login(_email['login'], _email['password'])
            for _unit in _payloads:
                _message = MIMEMultipart('alternative')
                _message['Subject'] = _unit['subject']
                _message['From'] = formataddr((str(Header(PAYLOAD['settings']['names']['from'], 'utf-8')), _email['login']))
                _message['To'] = _unit['to']
                _message.attach(MIMEText(getFormattedText('email/template.mail', {'mainbody': _unit['message'], 'year': str(datetime.now().year)}), _subtype='html'))
                _server.sendmail(_email['login'], _unit['to'], _message.as_string())
            alert('Успешно!', 'Почта в очереди была отправлена!')
            return True
        except Exception as e:
            alert('Ошибка!', str(e), 'warning')
            return False
        finally:
            _server.quit()
    else:
        return False

# Функция транслитерации кирилицы
def transliterateCyrilic(_string:str = ''):
    _alphabet = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'е': 'e',
        'ё': 'e',
        'ж': 'zh',
        'з': 'z',
        'и': 'i',
        'й': 'ii',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'y',
        'ф': 'f',
        'х': 'x',
        'ц': 'c',
        'ч': 'ch',
        'ш': 'sh',
        'щ': 'sh',
        'ъ': '',
        'ы': 'i',
        'ь': '',
        'э': 'e',
        'ю': 'yu',
        'я': 'ya',
        ' ': '.',
        '-': '.'
    }
    if len(_string) != 0:
        _returned = ''
        for _char in _string.lower():
            _returned += _alphabet[_char]
        return _returned
    else:
        return False

# Инициализация главной формы
class execute(QtWidgets.QMainWindow):
    def __init__(self):
        super(execute, self).__init__()
        self.ui = Ui_mainForm()
        self.ui.setupUi(self)
    def actionUpdateData_triggered(self):
        application.ui.treeOrgUnits.clear()
        results = DIRECTORY_API.orgunits().list(customerId='my_customer').execute()
        PAYLOAD.update({'orgUnits': collectOrgUnits(_orgUnits=results.get('organizationUnits'), _qTree = application.ui.treeOrgUnits)})
    def treeOrgUnits_itemSelected(self, _item, _id):
        _orgPath = []
        _subItem = _item
        while _subItem != None:
            _orgPath.append(_subItem.text(0))
            _subItem = _subItem.parent()
        _orgPath.reverse()
        _orgPath =  '/' + '/'.join(_orgPath)
        # print(_orgPath)
        _users = DIRECTORY_API.users().list(customer='my_customer', query='orgUnitPath=\'{}\''.format(_orgPath)).execute()
        self.ui.tableUsers.setRowCount(0)
        for _user in _users['users']:
            _position = self.ui.tableUsers.rowCount()
            self.ui.tableUsers.insertRow(_position)
            self.ui.tableUsers.setItem(_position, 0, QtWidgets.QTableWidgetItem(_user['name']['familyName']))
            self.ui.tableUsers.setItem(_position, 1, QtWidgets.QTableWidgetItem(_user['name']['givenName']))
            self.ui.tableUsers.setItem(_position, 2, QtWidgets.QTableWidgetItem(_user['primaryEmail']))
            self.ui.tableUsers.setItem(_position, 3, QtWidgets.QTableWidgetItem(_user['id']))
    def actionEmailSettings_triggered(self):
        _emailSettings.exec()
    def actionEmailCheckConnect_triggered(self):
        _checkEmail.exec()
    def buttonAddOrgUnit_clicked(self):
        print('Placeholder for buttonAddOrgUnit_clicked()')
    def buttonAddUser_clicked(self):
        _dialogRegUser.exec()
    def itemUsers_doubleClicked(self, _x, _y):
        EDITABLE_ID = int(self.ui.tableUsers.item(_x, 3).text())
        _user = DIRECTORY_API.users().get(userKey=EDITABLE_ID).execute()
        _dialogEditUser.ui.editLastName.setText(_user['name']['givenName'])
        _dialogEditUser.ui.editFirstName.setText(_user['name']['familyName'])
        _dialogEditUser.ui.editPrimaryEmail.setText(_user['primaryEmail'])
        _dialogEditUser.ui.editOrgUnitPath.setText(_user['orgUnitPath'])
        _subRecEmail = '' if _user.get('recoveryEmail') == None else _user['recoveryEmail']
        _dialogEditUser.ui.editRecoveryEmail.setText(_subRecEmail)
        _subRecPhone = '' if _user.get('phones') == None else _user['phones'][0]['value']
        _dialogEditUser.ui.editRecoveryMobilePhone.setText(_subRecPhone)
        _extId = '' if _user.get('externalIds') == None else _user['externalIds'][0]['value']
        _dialogEditUser.ui.editEmployeeId.setText(_extId)
        _addresses = {
            'work': '',
            'home': ''
        }
        if _user.get('addresses') != None:
            for _address in _user['addresses']:
                _addresses.update({_address['type']: '{}, "{}"'.format(_addresses[_address['type']], _address['formatted'])})
            _addresses.update({'work': _addresses['work'][2:]})
            _addresses.update({'home': _addresses['home'][2:]})
        _dialogEditUser.ui.editWorkAddress.setText(_addresses['work'])
        _dialogEditUser.ui.editHomeAddress.setText(_addresses['home'])
        if _user['suspended']:
            _dialogEditUser.ui.comboEmployeeStatus.setCurrentIndex(1)
        elif _user['archived']:
            _dialogEditUser.ui.comboEmployeeStatus.setCurrentIndex(2)
        else:
            _dialogEditUser.ui.comboEmployeeStatus.setCurrentIndex(0)
        if _user['changePasswordAtNextLogin']:
            _dialogEditUser.ui.comboChangePassword.setCurrentIndex(1)
        else:
            _dialogEditUser.ui.comboChangePassword.setCurrentIndex(0)
        _dialogEditUser.ui.editPassword.setText('****')
        _dialogEditUser.exec()


# Инициализация формы настройки файла электронной почты
class dialogEmailSettings(QtWidgets.QDialog):
    def __init__(self):
        super(dialogEmailSettings, self).__init__()
        self.ui = Ui_form_emailSettings()
        self.ui.setupUi(self)
    def buttonSave_clicked(self):
        if PAYLOAD.get('settings') == None:
            if (self.ui.editLogin.text() != '') & (self.ui.editPassword.text() != '') & (self.ui.editSMTPAddress.text() != '') & (self.ui.editSMTPPort.text() != ''):
                _settingsJSON = open(SETTINGS, mode='w')
                _settings = {
                    'email': {
                        'address': self.ui.editSMTPAddress.text(),
                        'port': self.ui.editSMTPPort.text(),
                        'login': self.ui.editLogin.text(),
                        'password': self.ui.editPassword.text()
                    }
                }
                _settingsJSON.write(json.dumps(_settings))
                PAYLOAD.update({'settings': _settings})
                _settingsJSON.close()
                self.close()
                application.show()
            else:
                alert('Внимание!', 'Все поля должны быть заполнены для сохранения!', 'warning')
        else:
            _settings = PAYLOAD['settings']
            _settings.update({
                'email': {
                        'address': self.ui.editSMTPAddress.text(),
                        'port': self.ui.editSMTPPort.text(),
                        'login': self.ui.editLogin.text(),
                        'password': self.ui.editPassword.text()
                    }
            })
            PAYLOAD.update({'settings': _settings})
            _settingsJSON = open(SETTINGS, mode='w')
            _settingsJSON.write(json.dumps(_settings))
            _settingsJSON.close()

# Инициализация формы загрузки CREDS-файла
class dialogJSONCreds(QtWidgets.QDialog):
    def __init__(self):
        super(dialogJSONCreds, self).__init__()
        self.ui = Ui_formJSONCreds()
        self.ui.setupUi(self)
    def buttonFile_clicked(self):
        _filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Открыть файл полномочий', '', 'JSON (*.json)', options=QtWidgets.QFileDialog.Options())
        if _filename:
            self.ui.lineEditFile.setText(_filename[0])
            copyfile(_filename[0], CREDENTIALS)
    def buttonSave_clicked(self):
        try:
            directoryAPI_exec()
        except ValueError:
            alert('Ошибка!', 'Предоставленный файл полномочий не обладает всеми полномочиями, либо он некорректный! Попробуйте ещё раз.', 'critical')
            os.remove(CREDENTIALS)
        else:
            self.close()

# Инициализация формы проверки подключения к сервису электронной почты
class dialogCheckEmail(QtWidgets.QDialog):
    def __init__(self):
        super(dialogCheckEmail, self).__init__()
        self.ui = Ui_form_checkEmail()
        self.ui.setupUi(self)
    def buttonSend_clicked(self):
        if self.ui.editEmail.text() != '':
            sendMail([{
                'to': self.ui.editEmail.text(),
                'subject': 'Проверка подключения к SMTP-серверу',
                'message': getFormattedText('email/checkConnect.mail')
            }])
        else:
            alert('Внимание!', 'Для того, чтобы проверить подключение, нужно ввести корректный адрес электронной почты!', 'warning')

# Инициализация формы редактирования пользователя
class dialogEditUser(QtWidgets.QDialog):
    def __init__(self):
        super(dialogEditUser, self).__init__()
        self.ui = Ui_form_editUser()
        self.ui.setupUi(self)
    def buttonSave_clicked(self):
        print('buttonSave_clicked')
    def buttonCreatePassword_clicked(self):
        if confirm('Подтвердите действие', 'Вы уверены, что хотите изменить пароль пользователю? Если у пользователя указан запасной адрес электронной почты, то ему придет письмо с новым паролем.\nТакже, пункт "Сменить пароль при следующем входе" будет установлен в значении "Да".'):
            self.ui.editPassword.setText(getRandomString(10))
            self.ui.comboChangePassword.setCurrentIndex(1)
    def buttonCreateEmployeeId_clicked(self):
        if PAYLOAD['settings'].get('employeeIdMask') != None:
            print('create employee id...')
        else:
            alert('Внимание!', 'Вы не можете создать уникальный идентификатор работника, т.к. у вас нет маски генерации уникального идентификатора работника!', 'warning')

# Инициализация формы регистрации пользователя или пользователей
class dialogRegUser(QtWidgets.QDialog):
    def __init__(self):
        super(dialogRegUser, self).__init__()
        self.ui = Ui_form_regUser()
        self.ui.setupUi(self)
    def buttonRegistration_clicked(self):
        if self.ui.labelCSVSearch.text() != '':
            if checkFileExsist(self.ui.labelCSVSearch.text()):
                    with open(self.ui.labelCSVSearch.text(), 'r') as _csv:
                        _reader = csv.DictReader(_csv)
                        _triggers = {
                            'primaryEmail': '',
                            'employeeId': '',
                            'isFirst': True
                        }
                        _formattedUsers = []
                        for _user in _reader:
                            if _triggers['isFirst']:
                                if (_user.get('lastname') != None) & (_user.get('firstname') != None) & (_user.get('recoveryEmail') != None) & (_user.get('primaryEmail') != None) & (_user.get('orgUnitPath') != None):
                                    _triggers.update({
                                        'primaryEmail': _user['primaryEmail'] if _user['primaryEmail'].find('@') == -1 else False,
                                        'employeeId': False if _user.get('employeeId') == None else ('auto' if _user['employeeId'] == 'auto' else 'manual')
                                    })
                                    _triggers.update({'isFirst': False})
                                else:
                                    alert('Внимание!', 'Не все обязательные поля указаны в таблице!', 'warning')
                                    break
                            _usersPayload = {
                                'lastname': _user['lastname'][0:1].upper() + _user['lastname'][1:].lower(),
                                'firstname': _user['firstname'][0:1].upper() + _user['firstname'][1:].lower(),
                                'recoveryEmail': _user['recoveryEmail'],
                                'primaryEmail': '{}.{}@{}'.format(transliterateCyrilic(_user['lastname']), transliterateCyrilic(_user['firstname']), _triggers['primaryEmail']) if _triggers['primaryEmail'] else _user['primaryEmail'],
                                'orgUnitPath': _user['orgUnitPath'],
                                'pasword': getRandomString(),
                                'recoveryPhone': _user['recoveryPhone'] if _user.get('recoveryPhone') != None else '',
                                'employeeId': '' if not _triggers['employeeId'] else ((_user['employeeId'] if _user.get('employeeId') != None else '') if _triggers['employeeId'] == 'manual' else 'autoDef'),
                                'workAddress': _user['workAddress'] if _user.get('workAddress') != None else '',
                                'homeAddress': _user['homeAddress'] if _user.get('homeAddress') != None else '',
                                'changePassword': True if _user.get('changePassword') == None else (True if _user['changePassword'] == "TRUE" else False),
                                'employeeStatus': 'Active' if _user.get('employeeStatus') == None else ('Active' if _user['employeeStatus'] == '' else _user['employeeStatus'])
                            }
                            if (_usersPayload['lastname'] != '') & (_usersPayload['firstname'] != '') & (_usersPayload['recoveryEmail'] != '') & (_usersPayload['primaryEmail'] != '') & (_usersPayload['orgUnitPath'] != ''):
                                _formattedUsers.append(_usersPayload)
                            else:
                                alert('Внимание!', 'У регистрируемых пользователей не хватает данных! Перепроверьте данные в таблице.', 'warning')
                        for _user in _formattedUsers:
                            print(_user)
            else:
                alert('Внимание!', 'Файл не найден!', 'warning')
        else:
            alert('Внимание!', 'Файл не выбран!', 'warning')
    def buttonCSVSearch_clicked(self):
        _filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Открыть файл с пользователями', '', 'CSV (*.csv)', options=QtWidgets.QFileDialog.Options())
        if _filename:
            self.ui.labelCSVSearch.setText(_filename[0])
    def buttonAdditionalInfo_clicked(self):
        webbrowser.open(getFullPath('resources/help/registration.html'), new=2)

# Конечная инициализация переменных оконных приложений
app = QtWidgets.QApplication([])

application = execute()
_dialogJSON = dialogJSONCreds()
_emailSettings = dialogEmailSettings()
_checkEmail = dialogCheckEmail()
_dialogEditUser = dialogEditUser()
_dialogRegUser = dialogRegUser()

# Подпрограмма запуска оконного приложения
try:
    DIRECTORY_API = directoryAPI_exec()
except ValueError:
    _dialogJSON.show()
else:
    if not DIRECTORY_API:
        _dialogJSON.show()
    else:
        results = DIRECTORY_API.orgunits().list(customerId='my_customer').execute()
        if not results.get('organizationUnits'):
            alert('Ошибка!', 'В вашем домене Google Workspace не создано ни одного огранизационного подразделения. Работа приложения невозможна.', 'critical')
        else:
            PAYLOAD.update({'orgUnits': collectOrgUnits(_orgUnits=results.get('organizationUnits'), _qTree = application.ui.treeOrgUnits)})
            if (checkFileExsist(SETTINGS)):
                _thumbSettings = open(SETTINGS, 'r')
                PAYLOAD.update({'settings': json.load(_thumbSettings)})
                _thumbSettings.close()

                application.show()

                _email = PAYLOAD['settings']['email']
                _emailSettings.ui.editLogin.setText(_email['login'])
                _emailSettings.ui.editPassword.setText(_email['password'])
                _emailSettings.ui.editSMTPAddress.setText(_email['address'])
                _emailSettings.ui.editSMTPPort.setText(_email['port'])

            else:
                _emailSettings.show()

sys.exit(app.exec())
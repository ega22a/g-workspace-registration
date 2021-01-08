# Импорт системных библиотек
from __future__ import print_function
from shutil import copyfile
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from PyQt5 import QtWidgets, QtCore
import sys, smtplib, json, ssl
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from email.header import Header
from string import Template
# Импорт форм
from form_mainForm import Ui_mainForm
from form_dialogJSONCreds import Ui_formJSONCreds
from form_alert import Ui_formAlert
from form_emailSettings import Ui_form_emailSettings
from form_checkEmail import Ui_form_checkEmail
from form_editUser import Ui_form_editUser

# Инициализация констант
SCOPES = [
    'https://www.googleapis.com/auth/admin.directory.user',
    'https://www.googleapis.com/auth/admin.directory.orgunit'
    ]
CREDENTIALS = 'credentials.json'
SETTINGS = 'settings.json'
EXEC_DIRECTORY = os.path.dirname(__file__)
DIRECTORY_API = None
PAYLOAD = {
    'orgUnits': None,
    'settings': None
}
application = None
_dialogAlert = None
_dialogJSON = None
_emailSettings = None
_checkEmail = None
_dialogEditUser = None

# Рекурсивная функция создания организационных подразделений
def collectOrgUnits(_orgUnits = None, _qTree = None):
    _returned = []
    for orgUnit in _orgUnits:
        _secReturn = {
            'name': orgUnit.get('name'),
            'orgUnitId': orgUnit.get('orgUnitId'),
            'orgUnitPath': orgUnit.get('orgUnitPath'),
            'in': None
        }
        _newTree = QtWidgets.QTreeWidgetItem(_qTree)
        _newTree.setText(0, orgUnit.get('name'))
        _check = DIRECTORY_API.orgunits().list(customerId='my_customer', orgUnitPath=orgUnit.get('orgUnitPath')).execute()
        if _check.get('organizationUnits'):
            _secReturn.update({'in': collectOrgUnits(_orgUnits = _check.get('organizationUnits'), _qTree = _newTree)})
        _returned.append(_secReturn)
    return _returned

# Функция проверки существования файла (относительные пути)
checkFileExsist = lambda _file: os.path.isfile(os.path.join(EXEC_DIRECTORY, _file))

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
        _emailSettings = PAYLOAD.get('settings').get('email')
        try:
            _server = smtplib.SMTP_SSL(_email.get('address'), int(_email.get('port')))
            _server.login(_email.get('login'), _email.get('password'))
            for _unit in _payloads:
                _message = MIMEMultipart('alternative')
                _message['Subject'] = _unit.get("subject")
                _message['From'] = formataddr((str(Header(PAYLOAD.get('settings').get('names').get('from'), 'utf-8')), _email.get('login')))
                _message['To'] = _unit.get('to')
                _message.attach(MIMEText(getFormattedText('email/template.mail', {'mainbody': _unit.get('message'), 'year': str(datetime.now().year)}), _subtype='html'))
                _server.sendmail(_email.get('login'), _unit.get('to'), _message.as_string())
            _dialogAlert.ui.labelMessage.setText("Почта в очереди была отправлена!")
            _dialogAlert.exec()
            return True
        except Exception as e:
            _dialogAlert.ui.labelMessage.setText(str(e))
            _dialogAlert.exec()
            return False
        finally:
            _server.quit()
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
        results = DIRECTORY_API.orgunits().list(customerId="my_customer").execute()
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
        for _user in _users.get('users'):
            _position = self.ui.tableUsers.rowCount()
            self.ui.tableUsers.insertRow(_position)
            self.ui.tableUsers.setItem(_position, 0, QtWidgets.QTableWidgetItem(_user.get('name').get('familyName')))
            self.ui.tableUsers.setItem(_position, 1, QtWidgets.QTableWidgetItem(_user.get('name').get('givenName')))
            self.ui.tableUsers.setItem(_position, 2, QtWidgets.QTableWidgetItem(_user.get('primaryEmail')))
            self.ui.tableUsers.setItem(_position, 3, QtWidgets.QTableWidgetItem(_user.get('id')))
    def actionEmailSettings_triggered(self):
        _emailSettings.exec()
    def actionEmailCheckConnect_triggered(self):
        _checkEmail.exec()
    def buttonAddOrgUnit_clicked(self):
        print("Placeholder for buttonAddOrgUnit_clicked()")
    def buttonAddUser_clicked(self):
        print("Placeholder for buttonAddUser_clicked()")
    def itemUsers_doubleClicked(self, _x, _y):
        _user = DIRECTORY_API.users().get(userKey=int(self.ui.tableUsers.item(_x, 3).text())).execute()
        _dialogEditUser.ui.editLastName.setText(_user.get('name').get('givenName'))
        _dialogEditUser.ui.editFirstName.setText(_user.get('name').get('familyName'))
        _dialogEditUser.ui.editPrimaryEmail.setText(_user.get('primaryEmail'))
        _dialogEditUser.ui.editOrgUnitPath.setText(_user.get('orgUnitPath'))
        _subRecEmail = '' if _user.get('recoveryEmail') == None else _user.get('recoveryEmail')
        _dialogEditUser.ui.editRecoveryEmail.setText(_subRecEmail)
        _subRecPhone = '' if _user.get('phones') == None else _user.get('phones')[0].get('value')
        _dialogEditUser.ui.editRecoveryMobilePhone.setText(_subRecPhone)
        _extId = '' if _user.get('externalIds') == None else _user.get('externalIds')[0].get('value')
        _dialogEditUser.ui.editEmployeeId.setText(_extId)
        _addresses = {
            'work': '',
            'home': ''
        }
        if _user.get('addresses') != None:
            for _address in _user.get('addresses'):
                _addresses.update({_address.get('type'): '{}, "{}"'.format(_addresses.get(_address.get('type')), _address.get('formatted'))})
            _addresses.update({'work': _addresses.get('work')[2:]})
            _addresses.update({'home': _addresses.get('home')[2:]})
        _dialogEditUser.ui.editWorkAddress.setText(_addresses.get('work'))
        _dialogEditUser.ui.editHomeAddress.setText(_addresses.get('home'))
        if _user.get('suspended'):
            _dialogEditUser.ui.comboEmployeeStatus.setCurrentIndex(1)
        elif _user.get('archived'):
            _dialogEditUser.ui.comboEmployeeStatus.setCurrentIndex(2)
        else:
            _dialogEditUser.ui.comboEmployeeStatus.setCurrentIndex(0)
        if _user.get('changePasswordAtNextLogin'):
            _dialogEditUser.ui.comboChangePassword.setCurrentIndex(1)
        else:
            _dialogEditUser.ui.comboChangePassword.setCurrentIndex(0)
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
                _dialogAlert.ui.labelMessage.setText('Все поля должны быть заполнены для сохранения!')
                _dialogAlert.exec()
        else:
            _settings = PAYLOAD.get('settings')
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

# Инициализация формы предупреждения
class dialogAlert(QtWidgets.QDialog):
    def __init__(self):
        super(dialogAlert, self).__init__()
        self.ui = Ui_formAlert()
        self.ui.setupUi(self)
    def buttonOk_clicked(self):
        self.hide()
        self.ui.labelMessage.setText("")

# Инициализация формы загрузки CREDS-файла
class dialogJSONCreds(QtWidgets.QDialog):
    def __init__(self):
        super(dialogJSONCreds, self).__init__()
        self.ui = Ui_formJSONCreds()
        self.ui.setupUi(self)
    def buttonFile_clicked(self):
        options = QtWidgets.QFileDialog.Options()
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "Открыть файл полномочий", "", "JSON (*.json)", options=options)
        if filename:
            self.ui.lineEditFile.setText(filename[0])
            copyfile(filename[0], CREDENTIALS)
    def buttonSave_clicked(self):
        try:
            directoryAPI_exec()
        except ValueError:
            _dialogAlert.ui.labelMessage.setText("Предоставленный файл полномочий не обладает всеми полномочиями, либо он некорректный! Попробуйте ещё раз.")
            os.remove(CREDENTIALS)
            _dialogAlert.exec()
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
            _dialogAlert.ui.labelMessage.setText('Для того, чтобы проверить подключение, нужно ввести корректный адрес электронной почты!')
            _dialogAlert.exec()

# Инициализация формы редактирования пользователя
class dialogEditUser(QtWidgets.QDialog):
    def __init__(self):
        super(dialogEditUser, self).__init__()
        self.ui = Ui_form_editUser()
        self.ui.setupUi(self)
    def buttonSave_clicked(self):
        print("buttonSave_clicked")
    def buttonCreatePassword_clicked(self):
        print("buttonCreatePasswrod_clicked")
    def buttonCreateEmployeeId_clicked(self):
        print("buttinCreateEmployeeId_clicked")

# Конечная инициализация переменных оконных приложений
app = QtWidgets.QApplication([])

application = execute()
_dialogAlert = dialogAlert()
_dialogJSON = dialogJSONCreds()
_emailSettings = dialogEmailSettings()
_checkEmail = dialogCheckEmail()
_dialogEditUser = dialogEditUser()

# Подпрограмма запуска оконного приложения
try:
    DIRECTORY_API = directoryAPI_exec()
except ValueError:
    _dialogJSON.show()
else:
    if not DIRECTORY_API:
        _dialogJSON.show()
    else:
        results = DIRECTORY_API.orgunits().list(customerId="my_customer").execute()
        if not results.get('organizationUnits'):
            _dialogAlert.ui.labelMessage.setText("В вашем домене Google Workspace не создано ни одного огранизационного подразделения. Работа приложения невозможна.")
            _dialogAlert.show()
        else:
            PAYLOAD.update({'orgUnits': collectOrgUnits(_orgUnits=results.get('organizationUnits'), _qTree = application.ui.treeOrgUnits)})
            if (checkFileExsist(SETTINGS)):
                _thumbSettings = open(SETTINGS, 'r')
                PAYLOAD.update({'settings': json.load(_thumbSettings)})
                _thumbSettings.close()

                application.show()

                _email = PAYLOAD.get('settings').get('email')
                _emailSettings.ui.editLogin.setText(_email.get('login'))
                _emailSettings.ui.editPassword.setText(_email.get('password'))
                _emailSettings.ui.editSMTPAddress.setText(_email.get("address"))
                _emailSettings.ui.editSMTPPort.setText(_email.get('port'))

            else:
                _emailSettings.show()

sys.exit(app.exec())
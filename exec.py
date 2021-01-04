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
# Импорт форм
from form_mainForm import Ui_mainForm
from form_dialogJSONCreds import Ui_formJSONCreds
from form_alert import Ui_formAlert
from form_emailSettings import Ui_form_emailSettings
from form_checkEmail import Ui_form_checkEmail

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
EMAIL = None
application = None
_dialogAlert = None
_dialogJSON = None
_emailSettings = None
_checkEmail = None

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
def checkFileExsist(_file):
    return os.path.isfile(os.path.join(EXEC_DIRECTORY, _file))

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

# Функция отправки писем через TLS SMTP
def sendMail(_destination = None, _subject = None, _text = None):
    if (PAYLOAD.get('settings') != None) & (_destination != None) & (_subject != None):
        _email = PAYLOAD.get('settings').get('email')
        # _context = ssl.create_default_context()
        try:
            _server = smtplib.SMTP_SSL(_email.get('address'), int(_email.get('port')))
            _server.login(_email.get('login'), _email.get('password'))
            _message = MIMEMultipart('alternative')
            _message['Subject'] = 'Проверка работоспособности smtplib'
            _message['From'] = _email.get('login')
            _message['To'] = _destination
            _message.attach(MIMEText("""
                <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" style="width:100%;font-family:arial, 'helvetica neue', helvetica, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0"><head><meta charset="UTF-8"><meta content="width=device-width, initial-scale=1" name="viewport"><meta name="x-apple-disable-message-reformatting"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta content="telephone=no" name="format-detection"><title>Новый шаблон</title> <!--[if (mso 16)]><style type="text/css">     a {text-decoration: none;}     </style><![endif]--> <!--[if gte mso 9]><style>sup { font-size: 100% !important; }</style><![endif]--> <!--[if gte mso 9]><xml> <o:OfficeDocumentSettings> <o:AllowPNG></o:AllowPNG> <o:PixelsPerInch>96</o:PixelsPerInch>
                </o:OfficeDocumentSettings> </xml><![endif]--><style type="text/css">
                #outlook a {	padding:0;}.ExternalClass {	width:100%;}.ExternalClass,.ExternalClass p,.ExternalClass span,.ExternalClass font,.ExternalClass td,.ExternalClass div {	line-height:100%;}.es-button {	mso-style-priority:100!important;	text-decoration:none!important;}a[x-apple-data-detectors] {	color:inherit!important;	text-decoration:none!important;	font-size:inherit!important;	font-family:inherit!important;	font-weight:inherit!important;	line-height:inherit!important;}.es-desk-hidden {	display:none;	float:left;	overflow:hidden;	width:0;	max-height:0;	line-height:0;	mso-hide:all;}@media only screen and (max-width:600px) {p, ul li, ol li, a { font-size:16px!important; line-height:150%!important } h1 { font-size:30px!important; text-align:center; line-height:120% } h2 { font-size:26px!important; text-align:center; line-height:120% } h3 { font-size:20px!important; text-align:center; line-height:120% } h1 a { font-size:30px!important } h2 a { 
                font-size:26px!important } h3 a { font-size:20px!important } .es-menu td a { font-size:16px!important } .es-header-body p, .es-header-body ul li, .es-header-body ol li, .es-header-body a { font-size:16px!important } .es-footer-body p, .es-footer-body ul li, .es-footer-body ol li, .es-footer-body a { font-size:16px!important } .es-infoblock p, .es-infoblock ul li, .es-infoblock ol li, .es-infoblock a { font-size:12px!important } *[class="gmail-fix"] { display:none!important } .es-m-txt-c, .es-m-txt-c h1, .es-m-txt-c h2, .es-m-txt-c h3 { text-align:center!important } .es-m-txt-r, .es-m-txt-r h1, .es-m-txt-r h2, .es-m-txt-r h3 { text-align:right!important } .es-m-txt-l, .es-m-txt-l h1, .es-m-txt-l h2, .es-m-txt-l h3 { text-align:left!important } .es-m-txt-r img, .es-m-txt-c img, .es-m-txt-l img { display:inline!important } .es-button-border { display:block!important } .es-btn-fw { border-width:10px 0px!important; 
                text-align:center!important } .es-adaptive table, .es-btn-fw, .es-btn-fw-brdr, .es-left, .es-right { width:100%!important } .es-content table, .es-header table, .es-footer table, .es-content, .es-footer, .es-header { width:100%!important; max-width:600px!important } .es-adapt-td { display:block!important; width:100%!important } .adapt-img { width:100%!important; height:auto!important } .es-m-p0 { padding:0px!important } .es-m-p0r { padding-right:0px!important } .es-m-p0l { padding-left:0px!important } .es-m-p0t { padding-top:0px!important } .es-m-p0b { padding-bottom:0!important } .es-m-p20b { padding-bottom:20px!important } .es-mobile-hidden, .es-hidden { display:none!important } tr.es-desk-hidden, td.es-desk-hidden, table.es-desk-hidden { width:auto!important; overflow:visible!important; float:none!important; max-height:inherit!important; line-height:inherit!important } tr.es-desk-hidden { display:table-row!important } 
                table.es-desk-hidden { display:table!important } td.es-desk-menu-hidden { display:table-cell!important } .es-menu td { width:1%!important } table.es-table-not-adapt, .esd-block-html table { width:auto!important } table.es-social { display:inline-block!important } table.es-social td { display:inline-block!important } a.es-button, button.es-button { font-size:20px!important; display:block!important; border-width:10px 0px 10px 0px!important } }</style></head><body style="width:100%;font-family:arial, 'helvetica neue', helvetica, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0"><div class="es-wrapper-color" style="background-color:#F6F6F6"> <!--[if gte mso 9]><v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t"> <v:fill type="tile" color="#f6f6f6"></v:fill> </v:background><![endif]-->
                <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;padding:0;Margin:0;width:100%;height:100%;background-repeat:repeat;background-position:center top"><tr style="border-collapse:collapse"><td valign="top" style="padding:0;Margin:0"><table cellpadding="0" cellspacing="0" class="es-header" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;background-color:transparent;background-repeat:repeat;background-position:center top"><tr style="border-collapse:collapse"><td align="center" style="padding:0;Margin:0"><table bgcolor="#ffffff" class="es-header-body" align="center" cellpadding="0" cellspacing="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;width:600px">
                <tr style="border-collapse:collapse"><td align="left" style="padding:0;Margin:0;padding-top:20px;padding-left:20px;padding-right:20px"> <!--[if mso]><table style="width:560px" cellpadding="0" cellspacing="0"><tr><td style="width:270px" valign="top"><![endif]--><table cellpadding="0" cellspacing="0" class="es-left" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left"><tr style="border-collapse:collapse"><td class="es-m-p0r es-m-p20b" valign="top" align="center" style="padding:0;Margin:0;width:270px"><table cellpadding="0" cellspacing="0" width="100%" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"><tr style="border-collapse:collapse"><td align="center" style="padding:0;Margin:0;font-size:0px">
                <img class="adapt-img" src="https://okptmc.stripocdn.email/content/guids/CABINET_f17bb2de294d5c72d027ebc0479224d8/images/10531609771525397.png" alt style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic" width="270"></td></tr></table></td></tr></table> <!--[if mso]></td><td style="width:20px"></td><td style="width:270px" valign="top"><![endif]--><table cellpadding="0" cellspacing="0" align="right" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"><tr style="border-collapse:collapse"><td align="left" style="padding:0;Margin:0;width:270px"><table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"><tr style="border-collapse:collapse"><td align="center" style="padding:0;Margin:0;display:none"></td></tr></table></td></tr></table> <!--[if mso]></td></tr></table>
                <![endif]--></td></tr></table></td></tr></table><table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%"><tr style="border-collapse:collapse"><td align="center" style="padding:0;Margin:0"><table class="es-content-body" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;width:600px" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center"><tr style="border-collapse:collapse"><td align="left" style="padding:0;Margin:0;padding-top:20px;padding-left:20px;padding-right:20px"><table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"><tr style="border-collapse:collapse">
                <td class="es-m-p0r es-m-p20b" valign="top" align="center" style="padding:0;Margin:0;width:560px"><table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"><tr style="border-collapse:collapse"><td align="center" style="padding:20px;Margin:0;font-size:0"><table border="0" width="100%" height="100%" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"><tr style="border-collapse:collapse"><td style="padding:0;Margin:0;border-bottom:1px solid #CCCCCC;background:none;height:1px;width:100%;margin:0px"></td></tr></table></td></tr><tr style="border-collapse:collapse"><td align="left" style="padding:0;Margin:0">
                <p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:14px;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333">""" + _text + """</p></td></tr><tr style="border-collapse:collapse"><td align="center" style="padding:20px;Margin:0;font-size:0"><table border="0" width="100%" height="100%" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"><tr style="border-collapse:collapse"><td style="padding:0;Margin:0;border-bottom:1px solid #CCCCCC;background:none;height:1px;width:100%;margin:0px"></td></tr></table></td></tr></table></td></tr></table></td></tr></table></td></tr></table>
                <table cellpadding="0" cellspacing="0" class="es-footer" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;background-color:transparent;background-repeat:repeat;background-position:center top"><tr style="border-collapse:collapse"><td align="center" style="padding:0;Margin:0"><table bgcolor="#ffffff" class="es-footer-body" align="center" cellpadding="0" cellspacing="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;width:600px"><tr style="border-collapse:collapse"><td align="left" style="Margin:0;padding-top:20px;padding-bottom:20px;padding-left:20px;padding-right:20px"> <!--[if mso]><table style="width:560px" cellpadding="0" cellspacing="0"><tr><td style="width:270px" valign="top"><![endif]-->
                <table cellpadding="0" cellspacing="0" class="es-left" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left"><tr style="border-collapse:collapse"><td class="es-m-p20b" align="left" style="padding:0;Margin:0;width:270px"><table cellpadding="0" cellspacing="0" width="100%" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"><tr style="border-collapse:collapse"><td align="left" style="padding:0;Margin:0"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:10px;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:15px;color:#333333">ГАПОУ СО "Нижнетагильский торгово-экономический колледж"&nbsp;© """ + str(datetime.now().year) + """ г.<br>Google LLC&nbsp;© """ + str(datetime.now().year) + """ г.</p></td></tr></table></td></tr></table> <!--[if mso]></td><td style="width:20px"></td>
                <td style="width:270px" valign="top"><![endif]--><table cellpadding="0" cellspacing="0" class="es-right" align="right" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:right"><tr style="border-collapse:collapse"><td align="left" style="padding:0;Margin:0;width:270px"><table cellpadding="0" cellspacing="0" width="100%" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"><tr style="border-collapse:collapse"><td align="left" style="padding:0;Margin:0"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:10px;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:15px;color:#333333">622001, Россия, Свердловская область, г. Нижний Тагил, пр. Ленина, д. 2а</p></td></tr></table></td></tr></table> <!--[if mso]></td></tr></table><![endif]--></td></tr></table>
                </td></tr></table></td></tr></table></div></body>
                </html>
            """, 'html'))
            _server.sendmail(_email.get('login'), _destination, _message.as_string())
            _dialogAlert.ui.labelMessage.setText("Письмо успешно отправлено!")
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
        print(_orgPath)
    def actionEmailSettings_triggered(self):
        _emailSettings.exec()
    def actionEmailCheckConnect_triggered(self):
        _checkEmail.exec()

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
class dialogCheckEmail(QtWidgets.QDialog):
    def __init__(self):
        super(dialogCheckEmail, self).__init__()
        self.ui = Ui_form_checkEmail()
        self.ui.setupUi(self)
    def buttonSend_clicked(self):
        if self.ui.editEmail.text() != '':
            sendMail(self.ui.editEmail.text(), 'Проверка подключения к SMTP-серверу...', 'Если вы это читаете, то это означает, что все работает корректно!')
        else:
            _dialogAlert.ui.labelMessage.setText('Для того, чтобы проверить подключение, нужно ввести корректный адрес электронной почты!')
            _dialogAlert.exec()

# Конечная инициализация переменных оконных приложений
app = QtWidgets.QApplication([])

application = execute()
_dialogAlert = dialogAlert()
_dialogJSON = dialogJSONCreds()
_emailSettings = dialogEmailSettings()
_checkEmail = dialogCheckEmail()

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
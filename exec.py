# Импорт системных библиотек
from __future__ import print_function
from shutil import copyfile
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from PyQt5 import QtWidgets, QtCore
import sys
# Импорт форм
from form_mainForm import Ui_mainForm
from form_dialogJSONCreds import Ui_formJSONCreds
from form_alert import Ui_formAlert

# Инициализация констант
SCOPES = [
    'https://www.googleapis.com/auth/admin.directory.user',
    'https://www.googleapis.com/auth/admin.directory.orgunit'
    ]
CREDENTIALS = 'credentials.json'
EXEC_DIRECTORY = os.path.dirname(__file__)
DIRECTORY_API = None
PAYLOAD = {
    'orgUnits': None
}
application = None
_dialogAlert = None
_dialogJSON = None

# Рекурсивная функция создания организационных подразделений
def collectOrgUnits(_orgUnits = None, _qTree = None):
    _returned = []
    for orgUnit in _orgUnits:
        _secReturn = {
            'name': orgUnit.get('name'),
            'orgUnitId': orgUnit.get('orgUnitId'),
            'orgUnitPath': orgUnit.get('orgUnitPath'),
            'in': None,
            'QtTreeWidgetItem': None
        }
        _newTree = QtWidgets.QTreeWidgetItem(_qTree)
        _newTree.setText(0, orgUnit.get('name'))
        _secReturn.update({'QtTreeWidgetItem': _newTree})
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
        service = build('admin', 'directory_v1', credentials=creds)
        return service
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
            DIRECTORY_API = directoryAPI_exec()
        except ValueError:
            _dialogAlert.ui.labelMessage.setText("Предоставленный файл полномочий не обладает всеми полномочиями, либо он некорректный! Попробуйте ещё раз.")
            os.remove(CREDENTIALS)
            _dialogAlert.exec()
        else:
            self.hide()
            application.show()

# Конечная инициализация переменных оконных приложений
app = QtWidgets.QApplication([])

application = execute()
_dialogAlert = dialogAlert()
_dialogJSON = dialogJSONCreds()

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
            application.show()

sys.exit(app.exec())
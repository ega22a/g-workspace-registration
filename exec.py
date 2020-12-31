# Импорт системных библиотек
from __future__ import print_function
from shutil import copyfile
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from PyQt5 import QtWidgets
import sys
# Импорт форм
from formsMainForm import Ui_mainForm
from form_dialogJSONCreds import Ui_formJSONCreds
from form_alert import Ui_formAlert

# Инициализация констант
SCOPES = ['https://www.googleapis.com/auth/admin.directory.user']
CREDENTIALS = 'credentials.json'
EXEC_DIRECTORY = os.path.dirname(__file__)
DIRECTORY_API = None

# Инициализация главной формы
class execute(QtWidgets.QMainWindow):
    def __init__(self):
        super(execute, self).__init__()
        self.ui = Ui_mainForm()
        self.ui.setupUi(self)
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

# Инициализация подключения к Directory API (Google Workspace)
def directoryAPI_exec():
    if (checkFileExsist(CREDENTIALS)):
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS, SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        service = build('admin', 'directory_v1', credentials=creds)
        return service
    else:
        return False

# Функция проверки существования файла (относительные пути)
def checkFileExsist(_file):
    return os.path.isfile(os.path.join(EXEC_DIRECTORY, _file))

# Конечная инициализация оконных приложений
app = QtWidgets.QApplication([])

application = execute()
_dialogAlert = dialogAlert()
_dialogJSON = dialogJSONCreds()

try:
    DIRECTORY_API = directoryAPI_exec()
except ValueError:
    _dialogJSON.show()
else:
    if not DIRECTORY_API:
        _dialogJSON.show()
    else:
        application.show()

sys.exit(app.exec())
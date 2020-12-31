# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_dialogJSONCreds.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_formJSONCreds(object):
    def setupUi(self, formJSONCreds):
        formJSONCreds.setObjectName("formJSONCreds")
        formJSONCreds.resize(400, 210)
        formJSONCreds.setMinimumSize(QtCore.QSize(400, 210))
        formJSONCreds.setMaximumSize(QtCore.QSize(400, 210))
        self.labelHeader = QtWidgets.QLabel(formJSONCreds)
        self.labelHeader.setGeometry(QtCore.QRect(10, 10, 381, 17))
        self.labelHeader.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.labelHeader.setObjectName("labelHeader")
        self.labelDescription = QtWidgets.QLabel(formJSONCreds)
        self.labelDescription.setGeometry(QtCore.QRect(10, 30, 381, 81))
        self.labelDescription.setWordWrap(True)
        self.labelDescription.setObjectName("labelDescription")
        self.horizontalLayoutWidget = QtWidgets.QWidget(formJSONCreds)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 120, 381, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelFile = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelFile.setObjectName("labelFile")
        self.horizontalLayout.addWidget(self.labelFile)
        self.lineEditFile = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEditFile.setEnabled(True)
        self.lineEditFile.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEditFile.setReadOnly(True)
        self.lineEditFile.setObjectName("lineEditFile")
        self.horizontalLayout.addWidget(self.lineEditFile)
        self.buttonFile = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonFile.setObjectName("buttonFile")
        self.horizontalLayout.addWidget(self.buttonFile)
        self.buttonSave = QtWidgets.QPushButton(formJSONCreds)
        self.buttonSave.setGeometry(QtCore.QRect(288, 170, 101, 25))
        self.buttonSave.setObjectName("buttonSave")

        self.retranslateUi(formJSONCreds)
        self.buttonFile.clicked.connect(formJSONCreds.buttonFile_clicked)
        self.buttonSave.clicked.connect(formJSONCreds.buttonSave_clicked)
        QtCore.QMetaObject.connectSlotsByName(formJSONCreds)

    def retranslateUi(self, formJSONCreds):
        _translate = QtCore.QCoreApplication.translate
        formJSONCreds.setWindowTitle(_translate("formJSONCreds", "Нет полномочий!"))
        self.labelHeader.setText(_translate("formJSONCreds", "<html><head/><body><p><span style=\" font-weight:600;\">ВНИМАНИЕ!</span></p></body></html>"))
        self.labelDescription.setText(_translate("formJSONCreds", "<html><head/><body><p>Для того, чтобы начать работу с программой, нужен файл полномочий в JSON-формате. Получить файл полномочий вы можете в Google Cloud Console (<a href=\"https://console.cloud.google.com/apis/credentials\"><span style=\" text-decoration: underline; color:#0000ff;\">ссылка</span></a>).</p></body></html>"))
        self.labelFile.setText(_translate("formJSONCreds", "Файл:"))
        self.buttonFile.setText(_translate("formJSONCreds", "Найти JSON..."))
        self.buttonSave.setText(_translate("formJSONCreds", "Сохранить"))
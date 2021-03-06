# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qt forms/form_emailSettings.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form_emailSettings(object):
    def setupUi(self, form_emailSettings):
        form_emailSettings.setObjectName("form_emailSettings")
        form_emailSettings.resize(401, 171)
        form_emailSettings.setMinimumSize(QtCore.QSize(401, 171))
        form_emailSettings.setMaximumSize(QtCore.QSize(401, 171))
        self.formLayoutWidget = QtWidgets.QWidget(form_emailSettings)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 161))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.editSMTPAddress = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.editSMTPAddress.setText("")
        self.editSMTPAddress.setObjectName("editSMTPAddress")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.editSMTPAddress)
        self.editSMTPPort = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.editSMTPPort.setObjectName("editSMTPPort")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.editSMTPPort)
        self.editLogin = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.editLogin.setObjectName("editLogin")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.editLogin)
        self.editPassword = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.editPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editPassword.setObjectName("editPassword")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.editPassword)
        self.buttonErase = QtWidgets.QPushButton(self.formLayoutWidget)
        self.buttonErase.setObjectName("buttonErase")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.buttonErase)
        self.buttonSave = QtWidgets.QPushButton(self.formLayoutWidget)
        self.buttonSave.setObjectName("buttonSave")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.buttonSave)

        self.retranslateUi(form_emailSettings)
        self.buttonErase.clicked.connect(self.editLogin.clear)
        self.buttonErase.clicked.connect(self.editPassword.clear)
        self.buttonErase.clicked.connect(self.editSMTPAddress.clear)
        self.buttonErase.clicked.connect(self.editSMTPPort.clear)
        self.buttonSave.clicked.connect(form_emailSettings.buttonSave_clicked)
        QtCore.QMetaObject.connectSlotsByName(form_emailSettings)

    def retranslateUi(self, form_emailSettings):
        _translate = QtCore.QCoreApplication.translate
        form_emailSettings.setWindowTitle(_translate("form_emailSettings", "Настройки электронной почты"))
        self.label.setText(_translate("form_emailSettings", "SMTP-адрес:"))
        self.label_2.setText(_translate("form_emailSettings", "Порт:"))
        self.label_3.setText(_translate("form_emailSettings", "Логин:"))
        self.label_4.setText(_translate("form_emailSettings", "Пароль:"))
        self.editSMTPAddress.setPlaceholderText(_translate("form_emailSettings", "Например, smtp.example.com"))
        self.editSMTPPort.setInputMask(_translate("form_emailSettings", "00000"))
        self.editSMTPPort.setPlaceholderText(_translate("form_emailSettings", "Например, 666"))
        self.buttonErase.setText(_translate("form_emailSettings", "Очистить"))
        self.buttonSave.setText(_translate("form_emailSettings", "Сохранить"))

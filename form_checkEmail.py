# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qt forms/form_checkEmail.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form_checkEmail(object):
    def setupUi(self, form_checkEmail):
        form_checkEmail.setObjectName("form_checkEmail")
        form_checkEmail.resize(401, 131)
        form_checkEmail.setMinimumSize(QtCore.QSize(401, 131))
        form_checkEmail.setMaximumSize(QtCore.QSize(401, 131))
        self.verticalLayoutWidget = QtWidgets.QWidget(form_checkEmail)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.editEmail = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.editEmail.setMinimumSize(QtCore.QSize(282, 0))
        self.editEmail.setObjectName("editEmail")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.editEmail)
        self.buttonSend = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.buttonSend.setObjectName("buttonSend")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.buttonSend)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(form_checkEmail)
        self.buttonSend.clicked.connect(form_checkEmail.buttonSend_clicked)
        QtCore.QMetaObject.connectSlotsByName(form_checkEmail)

    def retranslateUi(self, form_checkEmail):
        _translate = QtCore.QCoreApplication.translate
        form_checkEmail.setWindowTitle(_translate("form_checkEmail", "Проверка подключения к почте"))
        self.label.setText(_translate("form_checkEmail", "<html><head/><body><p align=\"center\">Проверка подключения к электронной почте</p><p>Для успешной проверки работоспособности сервиса отправки писем, введите адрес электронной почты, на который нужно отправить тестовое письмо.</p></body></html>"))
        self.editEmail.setPlaceholderText(_translate("form_checkEmail", "Адрес электронной почты"))
        self.buttonSend.setText(_translate("form_checkEmail", "Проверить"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qt forms/form_regUser.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form_regUser(object):
    def setupUi(self, form_regUser):
        form_regUser.setObjectName("form_regUser")
        form_regUser.setWindowModality(QtCore.Qt.NonModal)
        form_regUser.resize(781, 611)
        form_regUser.setMinimumSize(QtCore.QSize(781, 611))
        self.gridLayout_2 = QtWidgets.QGridLayout(form_regUser)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.buttonRegistration = QtWidgets.QPushButton(form_regUser)
        self.buttonRegistration.setObjectName("buttonRegistration")
        self.gridLayout.addWidget(self.buttonRegistration, 6, 0, 1, 2)
        self.label_18 = QtWidgets.QLabel(form_regUser)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 2, 0, 1, 2)
        self.label_19 = QtWidgets.QLabel(form_regUser)
        self.label_19.setWordWrap(True)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 3, 0, 1, 2)
        self.label_16 = QtWidgets.QLabel(form_regUser)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 0, 0, 1, 2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(form_regUser)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label)
        self.label_3 = QtWidgets.QLabel(form_regUser)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.editLastName = QtWidgets.QLineEdit(form_regUser)
        self.editLastName.setObjectName("editLastName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.editLastName)
        self.label_4 = QtWidgets.QLabel(form_regUser)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.editFirstName = QtWidgets.QLineEdit(form_regUser)
        self.editFirstName.setObjectName("editFirstName")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.editFirstName)
        self.label_5 = QtWidgets.QLabel(form_regUser)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.editPrimaryEmail = QtWidgets.QLineEdit(form_regUser)
        self.editPrimaryEmail.setObjectName("editPrimaryEmail")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.editPrimaryEmail)
        self.label_6 = QtWidgets.QLabel(form_regUser)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.editPassword = QtWidgets.QLineEdit(form_regUser)
        self.editPassword.setObjectName("editPassword")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.editPassword)
        self.label_7 = QtWidgets.QLabel(form_regUser)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.editOrgUnitPath = QtWidgets.QLineEdit(form_regUser)
        self.editOrgUnitPath.setObjectName("editOrgUnitPath")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.editOrgUnitPath)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_17 = QtWidgets.QLabel(form_regUser)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout.addWidget(self.label_17)
        self.labelCSVSearch = QtWidgets.QLineEdit(form_regUser)
        self.labelCSVSearch.setObjectName("labelCSVSearch")
        self.horizontalLayout.addWidget(self.labelCSVSearch)
        self.buttonCSVSearch = QtWidgets.QPushButton(form_regUser)
        self.buttonCSVSearch.setObjectName("buttonCSVSearch")
        self.horizontalLayout.addWidget(self.buttonCSVSearch)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 2)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_8 = QtWidgets.QLabel(form_regUser)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(form_regUser)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_10 = QtWidgets.QLabel(form_regUser)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_11 = QtWidgets.QLabel(form_regUser)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.label_12 = QtWidgets.QLabel(form_regUser)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.label_13 = QtWidgets.QLabel(form_regUser)
        self.label_13.setObjectName("label_13")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.label_14 = QtWidgets.QLabel(form_regUser)
        self.label_14.setObjectName("label_14")
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.label_15 = QtWidgets.QLabel(form_regUser)
        self.label_15.setObjectName("label_15")
        self.formLayout_3.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.label_2 = QtWidgets.QLabel(form_regUser)
        self.label_2.setMinimumSize(QtCore.QSize(396, 0))
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_2)
        self.buttonCreateEmployeeId = QtWidgets.QPushButton(form_regUser)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.buttonCreateEmployeeId.setFont(font)
        self.buttonCreateEmployeeId.setObjectName("buttonCreateEmployeeId")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.buttonCreateEmployeeId)
        self.editRecoveryEmail = QtWidgets.QLineEdit(form_regUser)
        self.editRecoveryEmail.setObjectName("editRecoveryEmail")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.editRecoveryEmail)
        self.editRecoveryMobilePhone = QtWidgets.QLineEdit(form_regUser)
        self.editRecoveryMobilePhone.setObjectName("editRecoveryMobilePhone")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.editRecoveryMobilePhone)
        self.editEmployeeId = QtWidgets.QLineEdit(form_regUser)
        self.editEmployeeId.setInputMask("")
        self.editEmployeeId.setObjectName("editEmployeeId")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.editEmployeeId)
        self.editWorkAddress = QtWidgets.QLineEdit(form_regUser)
        self.editWorkAddress.setObjectName("editWorkAddress")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.editWorkAddress)
        self.editHomeAddress = QtWidgets.QLineEdit(form_regUser)
        self.editHomeAddress.setObjectName("editHomeAddress")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.editHomeAddress)
        self.editNewPrimaryEmail = QtWidgets.QLineEdit(form_regUser)
        self.editNewPrimaryEmail.setObjectName("editNewPrimaryEmail")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.editNewPrimaryEmail)
        self.comboChangePassword = QtWidgets.QComboBox(form_regUser)
        self.comboChangePassword.setObjectName("comboChangePassword")
        self.comboChangePassword.addItem("")
        self.comboChangePassword.addItem("")
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.comboChangePassword)
        self.comboEmployeeStatus = QtWidgets.QComboBox(form_regUser)
        self.comboEmployeeStatus.setObjectName("comboEmployeeStatus")
        self.comboEmployeeStatus.addItem("")
        self.comboEmployeeStatus.addItem("")
        self.comboEmployeeStatus.addItem("")
        self.formLayout_3.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.comboEmployeeStatus)
        self.gridLayout.addLayout(self.formLayout_3, 1, 1, 1, 1)
        self.buttonAdditionalInfo = QtWidgets.QPushButton(form_regUser)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.buttonAdditionalInfo.setFont(font)
        self.buttonAdditionalInfo.setObjectName("buttonAdditionalInfo")
        self.gridLayout.addWidget(self.buttonAdditionalInfo, 4, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(form_regUser)
        self.buttonCreateEmployeeId.clicked.connect(form_regUser.buttonCreateEmployeeId_clicked)
        self.buttonAdditionalInfo.clicked.connect(form_regUser.buttonAdditionalInfo_clicked)
        self.buttonCSVSearch.clicked.connect(form_regUser.buttonCSVSearch_clicked)
        self.buttonRegistration.clicked.connect(form_regUser.buttonRegistration_clicked)
        QtCore.QMetaObject.connectSlotsByName(form_regUser)

    def retranslateUi(self, form_regUser):
        _translate = QtCore.QCoreApplication.translate
        form_regUser.setWindowTitle(_translate("form_regUser", "Редактировать пользователя"))
        self.buttonRegistration.setText(_translate("form_regUser", "Зарегистрировать"))
        self.label_18.setText(_translate("form_regUser", "<html><head/><body><p align=\"center\">Регистрация множества пользователей</p></body></html>"))
        self.label_19.setText(_translate("form_regUser", "<html><head/><body><p>Для множественной регистрации вам нужно создать CSV-таблицу в кодировке UTF-8. Используемый разделитель - знак запятой &quot;<span style=\" font-weight:600;\">,</span>&quot; (настоятельно рекомендуется использовать <a href=\"https://sheets.google.com\"><span style=\" text-decoration: underline; color:#0000ff;\">Google Таблицы</span></a>). Первая строка отводится под заголовки. Обязательные заголовки:</p>\n"
"<ol>\n"
"<li>lastname</li>\n"
"<li>firstname</li>\n"
"<li>primaryEmail</li>\n"
"<li>password</li>\n"
"<li>orgUnitPath</li>\n"
"</ol>\n"
"</body></html>"))
        self.label_16.setText(_translate("form_regUser", "<html><head/><body><p align=\"center\">Регистрация одного пользователя</p></body></html>"))
        self.label.setText(_translate("form_regUser", "<html><head/><body><p align=\"center\">Обязательные поля</p></body></html>"))
        self.label_3.setText(_translate("form_regUser", "Фамилия:"))
        self.editLastName.setToolTip(_translate("form_regUser", "<html><head/><body><p><span style=\" font-weight:600;\">Фамилия</span></p><p>Максимальное количество символов: 60.</p></body></html>"))
        self.label_4.setText(_translate("form_regUser", "Имя:"))
        self.editFirstName.setToolTip(_translate("form_regUser", "<html><head/><body><p><span style=\" font-weight:600;\">Имя</span></p><p>Максимальное количество символов: 60.</p></body></html>"))
        self.label_5.setText(_translate("form_regUser", "Электронная почта:"))
        self.editPrimaryEmail.setToolTip(_translate("form_regUser", "<html><head/><body><p><span style=\" font-weight:600;\">Электронная почта</span></p><p>Имя пользователя для входа. Введите адрес полностью: <span style=\" font-style:italic;\">imyapolzovatelya@vashdomen.com</span>.</p></body></html>"))
        self.label_6.setText(_translate("form_regUser", "Пароль:"))
        self.editPassword.setToolTip(_translate("form_regUser", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Пароль</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Пароли вводятся с учетом регистра. По умолчанию пароль должен содержать не менее 8 символов.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Если вы обновляете данные существующих пользователей и не хотите менять их пароли, введите <span style=\" font-weight:600;\">**** </span>(4 звездочки).</p></body></html>"))
        self.editPassword.setText(_translate("form_regUser", "****"))
        self.label_7.setText(_translate("form_regUser", "Орг. подразделение:"))
        self.editOrgUnitPath.setToolTip(_translate("form_regUser", "<html><head/><body><p><span style=\" font-weight:600;\">Организационное подразделение</span></p><p>Здесь указывается, к какому организационному подразделению относится пользователь.</p><p><span style=\" font-weight:600;\">Если вы ещё не создали организационную иерархию</span>, введите <span style=\" font-weight:600;\">только</span> косую черту (<span style=\" font-weight:600;\">/</span>), чтобы указать, что все пользователи относятся к <span style=\" font-weight:600;\">родительскому организационному подразделению верхнего уровня</span>. Вы можете создать другие подразделения позже и перенести туда пользователей.</p><p><span style=\" font-weight:600;\">Если вы уже создали организационную иерархию</span>, используйте показанный в примерах ниже формат, чтобы указать, к какому подразделению относится пользователь (родительского или дочернего уровня).</p><p>Примеры:</p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">/</span> (для <span style=\" font-weight:600;\">родительского подразделения верхнего уровня не указывайте</span> доменное имя;</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">/Продажи</span> (для дочерних подразделений);</li><li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">/Студенты/Первокурсники</span>.</li></ul></body></html>"))
        self.label_17.setText(_translate("form_regUser", "Файл:"))
        self.buttonCSVSearch.setText(_translate("form_regUser", "Найти CSV..."))
        self.label_8.setText(_translate("form_regUser", "Резервная эл. почта:"))
        self.label_9.setText(_translate("form_regUser", "Резервный моб. телефон:"))
        self.label_10.setText(_translate("form_regUser", "Личный номер сотрудника:"))
        self.label_11.setText(_translate("form_regUser", "Рабочий адрес:"))
        self.label_12.setText(_translate("form_regUser", "Домашний адрес:"))
        self.label_13.setText(_translate("form_regUser", "Новая основная эл. почта:"))
        self.label_14.setText(_translate("form_regUser", "Принудительная смена пароля:"))
        self.label_15.setText(_translate("form_regUser", "Статус сотрудника:"))
        self.label_2.setText(_translate("form_regUser", "<html><head/><body><p align=\"center\">Необязательные поля</p></body></html>"))
        self.buttonCreateEmployeeId.setText(_translate("form_regUser", "Сгенерировать личный номер"))
        self.editRecoveryEmail.setToolTip(_translate("form_regUser", "<html><head/><body><p><span style=\" font-weight:600;\">Резервный адрес электронной почты</span></p><p>Используйте адрес электронной почты, не входящий в ваш основной и дополнительные домены.</p></body></html>"))
        self.editRecoveryMobilePhone.setToolTip(_translate("form_regUser", "<html><head/><body><p><span style=\" font-weight:600;\">Резервный номер мобильного телефона</span></p><p>Указывайте номер телефона в формате <span style=\" font-weight:600;\">E.164</span> - сначала плюс (+), затем код страны, код региона и собственно номер. Пример: <span style=\" font-weight:600;\">+16505551212</span>.</p></body></html>"))
        self.editRecoveryMobilePhone.setInputMask(_translate("form_regUser", "+7 (000) 000 00-00"))
        self.editEmployeeId.setToolTip(_translate("form_regUser", "<html><head/><body><p><span style=\" font-weight:600;\">Идентификационный номер сотрудника</span></p><p>Иногда этот номер нужно указывать при дополнительной аутентификации. Он может содержать цифры, буквы и специальные символы.</p></body></html>"))
        self.editWorkAddress.setToolTip(_translate("form_regUser", "<html><head/><body><p><span style=\" font-weight:600;\">Рабочий адрес</span></p><p>Если адрес содержит запятые или переносы строки, заключите его в двойные кавычки. Пример: <span style=\" font-weight:600;\">&quot;Москва, улица Строителей, д. 25&quot;</span>.</p></body></html>"))
        self.editHomeAddress.setToolTip(_translate("form_regUser", "<html><head/><body><p><span style=\" font-weight:600;\">Домашний адрес</span></p><p>Если адрес содержит запятые или переносы строки, заключите его в двойные кавычки. Пример: <span style=\" font-weight:600;\">&quot;Москва, улица Строителей, д. 25&quot;</span>.</p></body></html>"))
        self.editNewPrimaryEmail.setToolTip(_translate("form_regUser", "<html><head/><body><p><span style=\" font-weight:600;\">Новый основной адрес электронной почты</span></p><p>Это поле исползуется только для редактирования аккаунтов существующих пользователей. Укажите новый основной адрес электронной почты (имя пользователя).</p></body></html>"))
        self.comboChangePassword.setToolTip(_translate("form_regUser", "<html><head/><body><p><span style=\" font-weight:600;\">Смена пароля при следующем входе</span></p><p>Чтобы при следующем входе в аккаунт пользователи получили запрос на смену пароля, выберите &quot;<span style=\" font-weight:600;\">Да</span>&quot;. Если этого не требуется, оставьте &quot;<span style=\" font-weight:600;\">Нет</span>&quot;.</p></body></html>"))
        self.comboChangePassword.setItemText(0, _translate("form_regUser", "Нет"))
        self.comboChangePassword.setItemText(1, _translate("form_regUser", "Да"))
        self.comboEmployeeStatus.setToolTip(_translate("form_regUser", "<html><head/><body><p><span style=\" font-weight:600;\">Новый статус сотрудника</span></p><p>Это поле используется только для редактирования аккаунтов <span style=\" font-weight:600;\">существующих </span>пользователей. Чтобы заблокировать пользователя или отправить его в архив, выберите <span style=\" font-weight:600;\">Suspended</span> или <span style=\" font-weight:600;\">Archived</span>. Чтобы восстановить аккаунт пользователя, выберите <span style=\" font-weight:600;\">Active</span>.</p></body></html>"))
        self.comboEmployeeStatus.setItemText(0, _translate("form_regUser", "Active"))
        self.comboEmployeeStatus.setItemText(1, _translate("form_regUser", "Suspended"))
        self.comboEmployeeStatus.setItemText(2, _translate("form_regUser", "Archived"))
        self.buttonAdditionalInfo.setText(_translate("form_regUser", "Дополнительная информация о регистрации через файл"))

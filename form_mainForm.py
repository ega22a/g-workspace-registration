# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qt forms/form_widgetMain.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainForm(object):
    def setupUi(self, mainForm):
        mainForm.setObjectName("mainForm")
        mainForm.setWindowModality(QtCore.Qt.ApplicationModal)
        mainForm.resize(800, 600)
        mainForm.setMinimumSize(QtCore.QSize(800, 600))
        mainForm.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(mainForm)
        self.centralwidget.setObjectName("centralwidget")
        self.treeOrgUnits = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeOrgUnits.setGeometry(QtCore.QRect(10, 10, 256, 561))
        self.treeOrgUnits.setColumnCount(1)
        self.treeOrgUnits.setObjectName("treeOrgUnits")
        self.tableUsers = QtWidgets.QTableWidget(self.centralwidget)
        self.tableUsers.setGeometry(QtCore.QRect(280, 10, 511, 561))
        self.tableUsers.setObjectName("tableUsers")
        self.tableUsers.setColumnCount(4)
        self.tableUsers.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableUsers.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUsers.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUsers.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUsers.setHorizontalHeaderItem(3, item)
        self.tableUsers.horizontalHeader().setDefaultSectionSize(127)
        self.tableUsers.verticalHeader().setDefaultSectionSize(31)
        self.tableUsers.verticalHeader().setMinimumSectionSize(21)
        mainForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menu)
        self.menu_2.setObjectName("menu_2")
        mainForm.setMenuBar(self.menubar)
        self.actionEmailCheckConnect = QtWidgets.QAction(mainForm)
        self.actionEmailCheckConnect.setObjectName("actionEmailCheckConnect")
        self.actionEmailSettings = QtWidgets.QAction(mainForm)
        self.actionEmailSettings.setObjectName("actionEmailSettings")
        self.actionGoogleWorkspace = QtWidgets.QAction(mainForm)
        self.actionGoogleWorkspace.setObjectName("actionGoogleWorkspace")
        self.actionDataUpdate = QtWidgets.QAction(mainForm)
        self.actionDataUpdate.setObjectName("actionDataUpdate")
        self.menu_2.addAction(self.actionEmailCheckConnect)
        self.menu_2.addAction(self.actionEmailSettings)
        self.menu.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.actionGoogleWorkspace)
        self.menu.addSeparator()
        self.menu.addAction(self.actionDataUpdate)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(mainForm)
        self.actionDataUpdate.triggered.connect(mainForm.actionUpdateData_triggered)
        self.treeOrgUnits.itemClicked['QTreeWidgetItem*','int'].connect(mainForm.treeOrgUnits_itemSelected)
        self.actionEmailSettings.triggered.connect(mainForm.actionEmailSettings_triggered)
        QtCore.QMetaObject.connectSlotsByName(mainForm)

    def retranslateUi(self, mainForm):
        _translate = QtCore.QCoreApplication.translate
        mainForm.setWindowTitle(_translate("mainForm", "Управление Google Workspace"))
        self.treeOrgUnits.headerItem().setText(0, _translate("mainForm", "Организационные подразделения"))
        item = self.tableUsers.horizontalHeaderItem(0)
        item.setText(_translate("mainForm", "Фамилия"))
        item = self.tableUsers.horizontalHeaderItem(1)
        item.setText(_translate("mainForm", "Имя"))
        item = self.tableUsers.horizontalHeaderItem(2)
        item.setText(_translate("mainForm", "Отчество"))
        item = self.tableUsers.horizontalHeaderItem(3)
        item.setText(_translate("mainForm", "Адрес электронной почты"))
        self.menu.setTitle(_translate("mainForm", "Настройки"))
        self.menu_2.setTitle(_translate("mainForm", "Электронная почта"))
        self.actionEmailCheckConnect.setText(_translate("mainForm", "Проверка подключения"))
        self.actionEmailSettings.setText(_translate("mainForm", "Настройка"))
        self.actionGoogleWorkspace.setText(_translate("mainForm", "Google Workspace"))
        self.actionDataUpdate.setText(_translate("mainForm", "Обновить данные"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Erfolgsberichte(object):
    def setupUi(self, Erfolgsberichte):
        Erfolgsberichte.setObjectName("Erfolgsberichte")
        Erfolgsberichte.resize(637, 664)
        self.centralwidget = QtWidgets.QWidget(Erfolgsberichte)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mw_sammeln_button = QtWidgets.QPushButton(self.centralwidget)
        self.mw_sammeln_button.setAutoDefault(False)
        self.mw_sammeln_button.setDefault(False)
        self.mw_sammeln_button.setFlat(False)
        self.mw_sammeln_button.setObjectName("mw_sammeln_button")
        self.horizontalLayout.addWidget(self.mw_sammeln_button)
        self.mw_button_new = QtWidgets.QPushButton(self.centralwidget)
        self.mw_button_new.setDefault(False)
        self.mw_button_new.setObjectName("mw_button_new")
        self.horizontalLayout.addWidget(self.mw_button_new)
        self.mw_button_show = QtWidgets.QPushButton(self.centralwidget)
        self.mw_button_show.setDefault(False)
        self.mw_button_show.setObjectName("mw_button_show")
        self.horizontalLayout.addWidget(self.mw_button_show)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.mw_ae_date_label = QtWidgets.QLabel(self.centralwidget)
        self.mw_ae_date_label.setObjectName("mw_ae_date_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.mw_ae_date_label)
        self.mw_ae_date = QtWidgets.QDateEdit(self.centralwidget)
        self.mw_ae_date.setCalendarPopup(True)
        self.mw_ae_date.setObjectName("mw_ae_date")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.mw_ae_date)
        self.mw_ae_cat_label = QtWidgets.QLabel(self.centralwidget)
        self.mw_ae_cat_label.setObjectName("mw_ae_cat_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.mw_ae_cat_label)
        self.mw_ae_cat = QtWidgets.QComboBox(self.centralwidget)
        self.mw_ae_cat.setObjectName("mw_ae_cat")
        self.mw_ae_cat.addItem("")
        self.mw_ae_cat.addItem("")
        self.mw_ae_cat.addItem("")
        self.mw_ae_cat.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.mw_ae_cat)
        self.mw_ae_text_label = QtWidgets.QLabel(self.centralwidget)
        self.mw_ae_text_label.setObjectName("mw_ae_text_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.mw_ae_text_label)
        self.mw_ae_text = QtWidgets.QTextEdit(self.centralwidget)
        self.mw_ae_text.setObjectName("mw_ae_text")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.mw_ae_text)
        self.mw_button_save = QtWidgets.QPushButton(self.centralwidget)
        self.mw_button_save.setDefault(False)
        self.mw_button_save.setFlat(True)
        self.mw_button_save.setObjectName("mw_button_save")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.mw_button_save)
        self.gridLayout_2.addLayout(self.formLayout, 4, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.mw_cr_button = QtWidgets.QPushButton(self.centralwidget)
        self.mw_cr_button.setObjectName("mw_cr_button")
        self.gridLayout.addWidget(self.mw_cr_button, 0, 3, 1, 1)
        self.mw_cr_cat_label = QtWidgets.QLabel(self.centralwidget)
        self.mw_cr_cat_label.setObjectName("mw_cr_cat_label")
        self.gridLayout.addWidget(self.mw_cr_cat_label, 0, 2, 1, 1)
        self.mw_cr_cat_box = QtWidgets.QComboBox(self.centralwidget)
        self.mw_cr_cat_box.setObjectName("mw_cr_cat_box")
        self.mw_cr_cat_box.addItem("")
        self.gridLayout.addWidget(self.mw_cr_cat_box, 1, 2, 1, 1)
        self.mw_cr_to_date = QtWidgets.QDateEdit(self.centralwidget)
        self.mw_cr_to_date.setCalendarPopup(True)
        self.mw_cr_to_date.setObjectName("mw_cr_to_date")
        self.gridLayout.addWidget(self.mw_cr_to_date, 1, 1, 1, 1)
        self.mw_cr_from_date = QtWidgets.QDateEdit(self.centralwidget)
        self.mw_cr_from_date.setWrapping(False)
        self.mw_cr_from_date.setCalendarPopup(True)
        self.mw_cr_from_date.setObjectName("mw_cr_from_date")
        self.gridLayout.addWidget(self.mw_cr_from_date, 0, 1, 1, 1)
        self.mw_cr_from_label = QtWidgets.QLabel(self.centralwidget)
        self.mw_cr_from_label.setObjectName("mw_cr_from_label")
        self.gridLayout.addWidget(self.mw_cr_from_label, 0, 0, 1, 1)
        self.mw_cr_to_label = QtWidgets.QLabel(self.centralwidget)
        self.mw_cr_to_label.setObjectName("mw_cr_to_label")
        self.gridLayout.addWidget(self.mw_cr_to_label, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.tabel_erfolge = QtWidgets.QTableWidget(self.centralwidget)
        self.tabel_erfolge.setAutoFillBackground(False)
        self.tabel_erfolge.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tabel_erfolge.setAlternatingRowColors(True)
        self.tabel_erfolge.setShowGrid(True)
        self.tabel_erfolge.setObjectName("tabel_erfolge")
        self.tabel_erfolge.setColumnCount(5)
        self.tabel_erfolge.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_erfolge.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_erfolge.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_erfolge.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_erfolge.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_erfolge.setHorizontalHeaderItem(4, item)
        self.tabel_erfolge.horizontalHeader().setDefaultSectionSize(150)
        self.tabel_erfolge.horizontalHeader().setStretchLastSection(True)
        self.tabel_erfolge.verticalHeader().setVisible(False)
        self.tabel_erfolge.verticalHeader().setDefaultSectionSize(25)
        self.tabel_erfolge.verticalHeader().setMinimumSectionSize(18)
        self.tabel_erfolge.verticalHeader().setSortIndicatorShown(True)
        self.tabel_erfolge.verticalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.tabel_erfolge, 6, 0, 1, 1)
        self.mw_feedback_label = QtWidgets.QLabel(self.centralwidget)
        self.mw_feedback_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mw_feedback_label.setFrameShape(QtWidgets.QFrame.Box)
        self.mw_feedback_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mw_feedback_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.mw_feedback_label.setObjectName("mw_feedback_label")
        self.gridLayout_2.addWidget(self.mw_feedback_label, 5, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_user = QtWidgets.QLabel(self.centralwidget)
        self.label_user.setObjectName("label_user")
        self.verticalLayout_2.addWidget(self.label_user)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 7, 0, 1, 1)
        Erfolgsberichte.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Erfolgsberichte)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 637, 21))
        self.menubar.setObjectName("menubar")
        Erfolgsberichte.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Erfolgsberichte)
        self.statusbar.setObjectName("statusbar")
        Erfolgsberichte.setStatusBar(self.statusbar)

        self.retranslateUi(Erfolgsberichte)
        QtCore.QMetaObject.connectSlotsByName(Erfolgsberichte)

    def retranslateUi(self, Erfolgsberichte):
        _translate = QtCore.QCoreApplication.translate
        Erfolgsberichte.setWindowTitle(_translate("Erfolgsberichte", "MainWindow"))
        self.mw_sammeln_button.setText(_translate("Erfolgsberichte", "Erfolge sammeln"))
        self.mw_button_new.setText(_translate("Erfolgsberichte", "neu"))
        self.mw_button_show.setText(_translate("Erfolgsberichte", "anzeigen"))
        self.mw_ae_date_label.setText(_translate("Erfolgsberichte", "Datum:"))
        self.mw_ae_cat_label.setText(_translate("Erfolgsberichte", "Bereich:"))
        self.mw_ae_cat.setItemText(0, _translate("Erfolgsberichte", "Arbeitsmarktintegration"))
        self.mw_ae_cat.setItemText(1, _translate("Erfolgsberichte", "Ehrenamt"))
        self.mw_ae_cat.setItemText(2, _translate("Erfolgsberichte", "Vernetzung"))
        self.mw_ae_cat.setItemText(3, _translate("Erfolgsberichte", "Sonstige"))
        self.mw_ae_text_label.setText(_translate("Erfolgsberichte", "Eintrag:"))
        self.mw_button_save.setText(_translate("Erfolgsberichte", "speichern"))
        self.mw_cr_button.setText(_translate("Erfolgsberichte", "Bericht ertellen"))
        self.mw_cr_cat_label.setText(_translate("Erfolgsberichte", "Bereich der Erfolge:"))
        self.mw_cr_cat_box.setItemText(0, _translate("Erfolgsberichte", "Alle"))
        self.mw_cr_from_label.setText(_translate("Erfolgsberichte", "von:"))
        self.mw_cr_to_label.setText(_translate("Erfolgsberichte", "bis:"))
        self.tabel_erfolge.setSortingEnabled(True)
        item = self.tabel_erfolge.horizontalHeaderItem(0)
        item.setText(_translate("Erfolgsberichte", "UID"))
        item = self.tabel_erfolge.horizontalHeaderItem(1)
        item.setText(_translate("Erfolgsberichte", "Datum"))
        item = self.tabel_erfolge.horizontalHeaderItem(2)
        item.setText(_translate("Erfolgsberichte", "FROM"))
        item = self.tabel_erfolge.horizontalHeaderItem(3)
        item.setText(_translate("Erfolgsberichte", "Bereich"))
        item = self.tabel_erfolge.horizontalHeaderItem(4)
        item.setText(_translate("Erfolgsberichte", "Erfolg"))
        self.mw_feedback_label.setText(_translate("Erfolgsberichte", "TextLabel"))
        self.label_user.setText(_translate("Erfolgsberichte", "TextLabel"))

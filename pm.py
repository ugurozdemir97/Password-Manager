from PyQt5 import QtCore, QtGui, QtWidgets


class Screen(object):
    def __init__(self):
        self.inform = None
        self.search = None
        self.remember = None
        self.password_label = None
        self.website_label = None
        self.my_passwords = None
        self.password_entry = None
        self.username_label = None
        self.generate = None
        self.about = None
        self.back = None
        self.passwords_page = None
        self.add = None
        self.username_entry = None
        self.website_entry = None
        self.logo = None
        self.stackedWidget = None
        self.main_page = None
        self.centralwidget = None
        self.table = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(887, 676)
        MainWindow.setFixedSize(887, 676)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 891, 681))
        self.stackedWidget.setObjectName("stackedWidget")
        self.main_page = QtWidgets.QWidget()
        self.main_page.setStyleSheet("#main_page {background-color: rgb(255, 255, 255);}")
        self.main_page.setObjectName("main_page")
        self.logo = QtWidgets.QLabel(self.main_page)
        self.logo.setGeometry(QtCore.QRect(250, 70, 401, 331))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/Image/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.website_entry = QtWidgets.QLineEdit(self.main_page)
        self.website_entry.setGeometry(QtCore.QRect(270, 430, 341, 31))
        self.website_entry.setStyleSheet("border: 1px solid rgb(200, 200, 200); border-radius: 5px; padding: 0 5px;")
        self.website_entry.setObjectName("website_entry")
        self.username_entry = QtWidgets.QLineEdit(self.main_page)
        self.username_entry.setGeometry(QtCore.QRect(270, 470, 341, 31))
        self.username_entry.setStyleSheet("border: 1px solid rgb(200, 200, 200); border-radius: 5px; padding: 0 5px;")
        self.username_entry.setObjectName("username_entry")
        self.password_entry = QtWidgets.QLineEdit(self.main_page)
        self.password_entry.setGeometry(QtCore.QRect(270, 510, 291, 31))
        self.password_entry.setStyleSheet("border: 1px solid rgb(200, 200, 200); border-radius: 5px;")
        self.password_entry.setObjectName("password_entry")
        self.website_label = QtWidgets.QLabel(self.main_page)
        self.website_label.setGeometry(QtCore.QRect(150, 430, 111, 31))
        self.website_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.website_label.setObjectName("website_label")
        self.username_label = QtWidgets.QLabel(self.main_page)
        self.username_label.setGeometry(QtCore.QRect(150, 470, 111, 31))
        self.username_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(self.main_page)
        self.password_label.setGeometry(QtCore.QRect(150, 510, 111, 31))
        self.password_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.password_label.setObjectName("password_label")
        self.remember = QtWidgets.QCheckBox(self.main_page)
        self.remember.setGeometry(QtCore.QRect(540, 550, 171, 31))
        self.remember.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.remember.setMouseTracking(False)
        self.remember.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.remember.setTristate(False)
        self.remember.setObjectName("remember")
        self.search = QtWidgets.QPushButton(self.main_page)
        self.search.setGeometry(QtCore.QRect(620, 430, 93, 31))
        self.search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search.setObjectName("search")
        self.generate = QtWidgets.QPushButton(self.main_page)
        self.generate.setGeometry(QtCore.QRect(570, 510, 141, 31))
        self.generate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.generate.setObjectName("generate")
        self.about = QtWidgets.QPushButton(self.main_page)
        self.about.setGeometry(QtCore.QRect(230, 550, 31, 31))
        self.about.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.about.setObjectName("about")
        self.add = QtWidgets.QPushButton(self.main_page)
        self.add.setGeometry(QtCore.QRect(620, 470, 93, 28))
        self.add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add.setObjectName("add")
        self.my_passwords = QtWidgets.QPushButton(self.main_page)
        self.my_passwords.setGeometry(QtCore.QRect(270, 550, 271, 31))
        self.my_passwords.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.my_passwords.setObjectName("my_passwords")
        self.stackedWidget.addWidget(self.main_page)
        self.passwords_page = QtWidgets.QWidget()
        self.passwords_page.setStyleSheet("#passwords_page {background-color: rgb(255, 255, 255);}")
        self.passwords_page.setObjectName("passwords_page")
        self.back = QtWidgets.QPushButton(self.passwords_page)
        self.back.setGeometry(QtCore.QRect(30, 610, 821, 28))
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back.setObjectName("back")
        self.inform = QtWidgets.QLabel(self.passwords_page)
        self.inform.setGeometry(QtCore.QRect(30, 20, 821, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.inform.setFont(font)
        self.inform.setAlignment(QtCore.Qt.AlignCenter)
        self.inform.setObjectName("inform")
        self.table = QtWidgets.QTableWidget(self.passwords_page)
        self.table.setGeometry(QtCore.QRect(50, 91, 781, 501))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.table.setFont(font)
        self.table.setAlternatingRowColors(True)
        self.table.setObjectName("table")
        self.table.setColumnCount(4)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(3, item)

        self.stackedWidget.addWidget(self.passwords_page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.website_entry.setPlaceholderText(_translate("MainWindow", "E.g: Amazon"))
        self.username_entry.setPlaceholderText(_translate("MainWindow", "E.g: amazon@gmail.com / E.g: amazon007"))
        self.website_label.setText(_translate("MainWindow", "Website:"))
        self.username_label.setText(_translate("MainWindow", "Username / Mail:"))
        self.password_label.setText(_translate("MainWindow", "Password:"))
        self.remember.setText(_translate("MainWindow", "Remember Username: "))
        self.search.setText(_translate("MainWindow", "Search"))
        self.generate.setText(_translate("MainWindow", "Generate Password"))
        self.about.setText(_translate("MainWindow", "?"))
        self.add.setText(_translate("MainWindow", "Add"))
        self.my_passwords.setText(_translate("MainWindow", "My Passwords"))
        self.back.setText(_translate("MainWindow", "Go Back"))
        self.inform.setText(_translate("MainWindow", "Click on columns to sort. Double click items to edit. "
                                                     "Press \"X\" to delete row"))
        self.table.setSortingEnabled(True)
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Website"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Username"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Password"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Delete"))

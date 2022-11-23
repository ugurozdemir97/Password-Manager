from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QTableWidgetItem, QHeaderView
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt
from random import choice, choices
from pm import Screen
from os import path, remove
import json
import sys
import source

LETTERS = ["Q", "W", "E", "T", "Y", "U", "I", "O", "P", "Ğ", "Ü", "A", "S", "D", "F", "G", "H", "J", "K", "L",
           "Ş", "İ", "Z", "X", "C", "V", "B", "N", "M", "Ö", "Ç", "q", "w", "e", "r", "t", "y", "u", "ı", "o",
           "p", "ğ", "ü", "a", "s", "d", "f", "g", "h", "j", "k", "l", "ş", "i", "z", "x", "c", "v", "b", "n",
           "m", "ö", "ç"]
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SYMBOLS = ["!", "&", "+", "#", "*", "/", "$", "%", "(", ")"]
ALL_CHARACTERS = [LETTERS, NUMBERS, SYMBOLS]


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()

        self.ui = Screen()
        self.ui.setupUi(self)

        self.turn_main_menu = None  # This will be used to edit passwords when turning back to main menu

        # --------- LOAD PASSWORDS IF EXIST --------- #

        try:
            with open("Data/Passwords.json", "r") as data:
                self.passwords = json.load(data)
        except FileNotFoundError:
            self.passwords = []

        # --------- LOAD USERNAME IF EXIST --------- #

        try:
            with open("Username.json", "r") as data:
                self.ui.username_entry.setText(json.load(data))
        except FileNotFoundError:
            pass
        else:
            self.ui.remember.setText("Delete Username: ")

        # ---------------------- BUTTONS --------------------- #

        self.ui.generate.clicked.connect(self.generate)
        self.ui.add.clicked.connect(self.add)
        self.ui.my_passwords.clicked.connect(self.show_passwords)
        self.ui.search.clicked.connect(self.show_passwords)
        self.ui.back.clicked.connect(self.main)
        self.ui.about.clicked.connect(self.about)

    # ------------------------------ ABOUT PAGE ----------------------------- #

    @staticmethod
    def about():
        msg = QMessageBox()
        msg.setWindowTitle("Password Manager")
        msg.setText("This program allows you to save and organise your passwords and does not encrypt them. \n"
                    "You can generate strong passwords or search if you have a password for a website.\n"
                    "                                               Written by Uğur Özdemir in 2022.")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    # ---------------- RETURN BACK TO THE MAIN PAGE & RECREATE PASSWORDS DATA ------------------ #

    def main(self):

        # If we turned back from Search, then we will append self.passwords, otherwise we will recreate self.passwords.

        if self.turn_main_menu == "Search":
            pass
        else:
            self.passwords = []

        self.turn_main_menu = None

        # --------------- SAVE NEW PASSWORDS IF THERE IS ANY CHANGE ------------ #

        for row in range(self.ui.table.rowCount()):  # Row Count
            dictionary = {
                "Website": self.ui.table.item(row, 0).text(),
                "Username / Mail": self.ui.table.item(row, 1).text(),
                "Passwords": self.ui.table.item(row, 2).text()
            }
            self.passwords.append(dictionary)
        self.ui.table.clearContents()

        # ----- UPDATE FILE ----- #

        with open("Data/Passwords.json", "w") as data:
            json.dump(self.passwords, data, indent=4)

        self.ui.stackedWidget.setCurrentIndex(0)

    # --------------------------------- GENERATE PASSWORDS --------------------------------- #

    def generate(self):
        password = ""
        for i in range(15):
            password += choice(choices(ALL_CHARACTERS, weights=(60, 30, 10))[0])

        self.ui.password_entry.setText(password)

        # choices(ALL_CHARACTERS, weights=(60, 30, 10))[0] returns a letter list or number list, or symbol list with
        # different probabilities. Then choose a random item from that list using choice.

    # ---------------------------------- ADD NEW PASSWORD --------------------------------- #

    def add(self):
        website = self.ui.website_entry.text()
        username = self.ui.username_entry.text()
        password = self.ui.password_entry.text()

        # ------- Clear Texts ------- #

        self.ui.website_entry.setText("")
        self.ui.username_entry.setText("")
        self.ui.password_entry.setText("")

        # ------- Save/Delete Username if Remember/Delete is Checked ----- #

        if self.ui.remember.isChecked():
            if username != "":
                self.ui.remember.setCheckState(False)
                if self.ui.remember.text() == "Remember Username: ":
                    self.ui.remember.setText("Delete Username: ")
                    with open("Username.json", "w") as data:
                        json.dump(username, data)
                else:
                    self.ui.remember.setText("Remember Username: ")
                    if path.exists("Username.json"):
                        remove("Username.json")

        # --------- Warn if there are empty fields --------- #

        if website == "" or username == "" or password == "":
            msg = QMessageBox()
            msg.warning(self, "Empty Entry", "Please don't leave any fields empty!", QMessageBox.Ok)

        else:

            # ---------------- Update password JSON -------------------- #

            new_pass = {"Website": website, "Username / Mail": username, "Passwords": password}
            self.passwords.append(new_pass)

            with open("Data/Passwords.json", "w") as data:
                json.dump(self.passwords, data, indent=4)

    # ---------------------------------- SHOW MY PASSWORDS --------------------------------- #

    def show_passwords(self):

        sender = self.sender()
        self.ui.table.setSortingEnabled(False)  # You should set sorting to False before you create the table, and
        # enable it after you create it. Because otherwise the program crushes if you sort the table and then search
        # something. This problem is I think from PyQt library itself.

        # ------------- Set Column Width -------------- #

        header = self.ui.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Fixed)
        self.ui.table.setColumnWidth(3, 80)

        if sender.text() == "Search":  # If you clicked search show only the relevant data

            self.turn_main_menu = "Search"

            # ------------------------ GET SEARCH RESULT ------------------------ #

            found = list(filter(lambda row: row["Website"] == self.ui.website_entry.text(), self.passwords))
            self.ui.table.setRowCount(len(found))

            # Remove found items from the passwords list.
            self.passwords = list(filter(lambda row: row["Website"] != self.ui.website_entry.text(), self.passwords))

            # -------------------------- CREATE TABLE --------------------------- #

            for x, item in enumerate(found):

                # -------------- Add delete button to each row -------------- #

                delete = QPushButton("X")
                delete.clicked.connect(self.delete)
                delete.setCursor(QCursor(Qt.PointingHandCursor))
                self.ui.table.setCellWidget(x, 3, delete)

                # ----------------------- Place Items ----------------------- #

                for y, value in enumerate(item.items()):
                    item = QTableWidgetItem()
                    item.setTextAlignment(Qt.AlignCenter)
                    item.setText(value[1])
                    self.ui.table.setItem(x, y, item)

        else:  # Show all passwords.
            self.ui.table.setRowCount(len(self.passwords))  # Set row count

            self.turn_main_menu = "All"

            # -------------------------- CREATE TABLE --------------------------- #

            for x, item in enumerate(self.passwords):

                # -------------- Add delete button to each row -------------- #

                delete = QPushButton("X")
                delete.clicked.connect(self.delete)
                delete.setCursor(QCursor(Qt.PointingHandCursor))
                self.ui.table.setCellWidget(x, 3, delete)

                # ----------------------- Place Items ----------------------- #

                for y, value in enumerate(item.items()):
                    item = QTableWidgetItem()
                    item.setTextAlignment(Qt.AlignCenter)
                    item.setText(value[1])
                    self.ui.table.setItem(x, y, item)

        self.ui.table.setSortingEnabled(True)

        # Delete texts if exist
        self.ui.website_entry.setText("")
        self.ui.username_entry.setText("")
        self.ui.password_entry.setText("")

        self.ui.stackedWidget.setCurrentIndex(1)

    # ---------------------------------- DELETE PASSWORD ROW --------------------------------- #

    def delete(self):
        button = self.sender()
        if button:
            row = self.ui.table.indexAt(button.pos()).row()
            self.ui.table.removeRow(row)


def application():
    window = QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(window.exec_())


application()

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFrame, QSlider, QLabel, QPushButton, QLineEdit, QCheckBox, QMessageBox
from PyQt5.QtCore import QPropertyAnimation, QRect, QPoint
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import uic
import sys
import random
import string


class PG(QMainWindow):
    def __init__(self):
        super(PG, self).__init__()
        uic.loadUi("PG.ui", self)
        # Window title and icon

        self.setWindowTitle("Password Generator App")
        self.setWindowIcon(QIcon("icon.png"))
        # import widgets from ui file and define
        self.length_slider = self.findChild(QSlider, "length_slider")
        self.slider_value_label = self.findChild(QLabel, "slider_value_label")
        self.upper_chBox = self.findChild(QCheckBox, "upper_chBox")
        self.number_chBox = self.findChild(QCheckBox, "number_chBox")
        self.symbol_chBox = self.findChild(QCheckBox, "symbol_chBox")
        self.lower_chBox = self.findChild(QCheckBox, "lower_chBox")
        self.password_label = self.findChild(QLabel, "password_label")
        self.passwordQuality_label = self.findChild(
            QLabel, "passwordQuality_label")
        self.clear_pushButton = self.findChild(QPushButton, "clear_pushButton")
        self.copy_pushButton = self.findChild(QPushButton, "copy_pushButton")
        # Set lowercase charecters as default
        self.lower_chBox.setChecked(True)
        # connect slider and pushbutton to functions
        self.length_slider.valueChanged.connect(self.generate)
        self.clear_pushButton.clicked.connect(self.clear)
        self.copy_pushButton.clicked.connect(self.copyToClipboard)
        # Password Charecters Definition:number,lowercase,uppercase,symbol
        self.numbers = string.digits
        self.lowercase_chars = string.ascii_lowercase
        self.uppercase_chars = string.ascii_uppercase
        self.symbols = string.punctuation
        # shows the  app
        self.show()

    # Check which checkBox is checked or not
    def check_chBox(self):
        self.temp_password = ""
        if (self.lower_chBox.isChecked()) == True:
            self.temp_password += self.lowercase_chars
        if (self.number_chBox.isChecked()) == True:
            self.temp_password += self.numbers
        if (self.upper_chBox.isChecked()) == True:
            self.temp_password += self.uppercase_chars
        if (self.symbol_chBox.isChecked()) == True:
            self.temp_password += self.symbols

    # generate random password according to length and checkBoxes
    def generate(self, val):
        try:
            # update the temp password
            self.check_chBox()
            self.slider_value_label.setText(str(val))
            self. length = val
            self.final_password = "".join(
                random.sample(self.temp_password, self.length))
            self.password_label.setText(self.final_password)
            self. password_quality()
        except:
            self.messageBox("Length Error")

    # specify final password's security: bad,weak or strong

    def password_quality(self):

        if (self.length >= 1 and self.length <= 5):
            self.passwordQuality_label.setText("Bad password")
            self.password_label.setStyleSheet(
                "QLabel#password_label{background-color:#EB1D36;border-radius:20px;}")
            self.passwordQuality_label.setStyleSheet(
                "QLabel#passwordQuality_label{color:#EB1D36;}")
        elif (self.length >= 6 and self.length <= 10):
            self.passwordQuality_label.setText("Weak password")
            self.password_label.setStyleSheet(
                "QLabel#password_label{background-color:#FA9494;border-radius:20px;}")
            self.passwordQuality_label.setStyleSheet(
                "QLabel#passwordQuality_label{color:#FA9494;}")
        elif (self.length >= 11 and self.length <= 52):
            self.passwordQuality_label.setText("Strong password")
            self.password_label.setStyleSheet(
                "QLabel#password_label{background-color:#5BB318;border-radius:20px;}")
            self.passwordQuality_label.setStyleSheet(
                "QLabel#passwordQuality_label{color:#5BB318;}")
    # clear passwordQuality label,unckecks checkBoxes and set the slider value to 0

    def clear(self):
        self.length_slider.setValue(0)
        self.lower_chBox.setChecked(True)
        self.upper_chBox.setChecked(False)
        self.number_chBox.setChecked(False)
        self.symbol_chBox.setChecked(False)
        self.passwordQuality_label.setText("Quality")
        self.password_label.setStyleSheet(
            "QLabel#password_label{background-color:#D1D1D1;border-radius:20px;}")
        self.passwordQuality_label.setStyleSheet(
            "QLabel#passwordQuality_label{color:#000000;}")
    # Show Message Box:Length Error-Empty password errorl-copy to clipboard successfuly

    def messageBox(self, message):
        msg_box = QMessageBox()
        if (message == "Length Error"):
            msg_box.setWindowTitle("Length error")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText(
                "To have longer passwrod choose more charecter options")
            msg_box.setStandardButtons(QMessageBox.Ok)
        elif (message == "Empty"):
            msg_box.setWindowTitle("Empty")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("You haven't generated any password yet")
            msg_box.setStandardButtons(QMessageBox.Ok)
        elif (message == "copied"):
            msg_box.setWindowTitle("Copied to clipboard")
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Your password copied!")
            msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

    def copyToClipboard(self):
        if self.password_label.text() == "":
            self.messageBox("Empty")
        else:
            copy_to_clipboard = QApplication.clipboard()
            copy_to_clipboard.clear(mode=copy_to_clipboard.Clipboard)
            copy_to_clipboard.setText(
                self.password_label.text(), mode=copy_to_clipboard.Clipboard)
            self.messageBox("copied")


app = QApplication(sys.argv)
UIwindow = PG()
app.exec_()

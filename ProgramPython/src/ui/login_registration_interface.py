from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import QtGui, QtWidgets, QtCore

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 550)
        font = QtGui.QFont()
        font.setFamily("Arial")
        Form.setFont(font)

        self.setup_styles(Form)
        self.setup_widgets(Form)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def setup_styles(self, Form):
        style_sheet = """
            QPushButton#pushButton, #pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5 {    
                background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));
                color: rgba(255, 255, 255, 210);
                border-radius: 5px;
            }
            QPushButton#pushButton:hover, #pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover {    
                background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));
            }
            QPushButton#pushButton:pressed, #pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed {    
                padding-left: 5px;
                padding-top: 5px;
                background-color: rgba(105, 118, 132, 200);
            }
        """
        Form.setStyleSheet(style_sheet)

    def setup_widgets(self, Form):
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 30, 370, 480))

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 30, 300, 420))
        self.label.setStyleSheet("border-image: url(images/background.png);\n"
                                "border-radius:20px;")
        self.label.setText("")

        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 300, 420))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.715909, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 50), stop:0.835227 rgba(0, 0, 0, 75));\n"
                                   "border-radius:20px;")
        self.label_2.setText("")

        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(140, 90, 81, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(255, 255, 255, 210);")

        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 165, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                    "border:none;\n"
                                    "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
                                    "color:rgba(255, 255, 255, 230);\n"
                                    "padding-bottom:7px;")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 230, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                      "border:none;\n"
                                      "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
                                      "color:rgba(255, 255, 255, 230);\n"
                                      "padding-bottom:7px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        # Close
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(80, 310, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 35, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setText("X")
        self.pushButton_2.setStyleSheet("background: transparent; border: none; color: white;")
        self.pushButton_2.clicked.connect(Form.close)
        # Minimize
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 26, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setText("_")
        self.pushButton_3.setStyleSheet("background: transparent; border: none; color: white;")
        self.pushButton_3.clicked.connect(Form.showMinimized)
        # Maximize
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 32, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setText("□")  # Square symbol for maximize
        self.pushButton_4.setStyleSheet("background: transparent; border: none; color: white;")
        self.pushButton_4.clicked.connect(self.toggle_maximized)  # Connect to a function to toggle between maximized and restored

    def toggle_maximized(self, Form):
        if Form.isMaximized():
            Form.showNormal()
        else:
            Form.showMaximized()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login Form"))
        self.label_4.setText(_translate("Form", "Login"))
        self.lineEdit.setPlaceholderText(_translate("Form", "  Username"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "  Password"))
        self.pushButton.setText(_translate("Form", "Login"))

class LoginRegistrationInterface(QWidget, Ui_Form):
    def __init__(self, database):
        super().__init__()
        self.database = database
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setupUi(self)
        self.init_custom_ui()
        
    def init_custom_ui(self):
        self.pushButton.clicked.connect(self.process_action)
        self.pushButton_registration = self.create_button("Register", QtCore.QRect(110, 390, 200, 41))  # Registration button on the initial screen
        self.pushButton_registration.clicked.connect(self.toggle_registration_login)
        self.registration = False

    def toggle_registration_login(self):
        self.clear_fields()
        if not self.registration:
            self.pushButton.setText("Register")  # Button name
            self.label_4.setText("Registration")  # Text name on the screen
        else:
            self.pushButton.setText("Login")
            self.label_4.setText("Login")
        self.registration = not self.registration

    def process_action(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if not username or not password:
            QMessageBox.critical(self, 'Error', 'Please fill in all fields.')
            return

        if self.registration:
            registration_success = self.database.register(username, password)
            if registration_success:
                QMessageBox.information(self, 'Registration', 'Registration successful!')
                self.clear_fields()
                self.toggle_registration_login()  # Switch to the login screen
            else:
                QMessageBox.critical(self, 'Registration Error', 'Username already in use. Choose another name.')
        else:
            if self.database.login(username, password):
                QMessageBox.information(self, 'Successful Login', 'Login successful!')
            else:
                QMessageBox.critical(self, 'Login Error', 'Invalid credentials. Please try again.')

    def clear_fields(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()

    def create_button(self, text, geometry):
        button = QtWidgets.QPushButton(self)
        button.setGeometry(geometry)
        button.setText(text)
        return button

import sys
from PyQt5.QtWidgets import QApplication
from src.ui.login_registration_interface import LoginRegistrationInterface
from src.database import Database

def run_app():
    app = QApplication(sys.argv)
    database = Database()
    window = LoginRegistrationInterface(database)
    window.show()
    sys.exit(app.exec_())

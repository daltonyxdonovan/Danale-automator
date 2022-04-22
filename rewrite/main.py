from PyQt5.QtWidgets import (QToolTip,QRadioButton, QLabel, QPushButton, QPlainTextEdit, QGridLayout, QWidget, QLineEdit, QProgressBar)
from PyQt5.QtCore import QProcess
from qtpy import QtWidgets
from PyQt5.QtGui import QFont
import sys, re, os, qdarkstyle, csv, time, shutil, pickle
from datetime import datetime
from datetime import timedelta
import readery

os.environ['QT_API'] = 'pyqt5'
cwd = os.getcwd()

 
class GUI(QWidget):
    days = 0
    def message(self, s):
        self.textbox.appendPlainText(s)
    def handle_stderr(self):
        self.p = QProcess()
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.message(stderr)
    def handle_stdout(self):
        self.p = QProcess()
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.message(stdout)
    def detectName(rows):
        if "rent" in rows[11] or "Rent" in rows[11]:
            return str("Rent")
        elif "Google" in rows[11]:
            return str("Google")
        elif "Spotify" in rows[11]:
            return str("Spotify")
        elif "EDUCATION" in rows[11]:
            return str("Typing Class")
        elif "Pandora" in rows[11]:
            return str("Pandora")
        elif "Youtube" in rows[11]:
            return str("TV")
        elif "Netflix" in rows[11] or "NETFLIX" in rows[11]:
            return str("TV")
        elif "Amazon" in rows[11] or "AMZN" in rows[11] or "AMAZON" in rows[11]:
            return str("Amazon")
        elif "SLIDE" in rows[11] or "Speedway" in rows[11] or "GAS" in rows[11]:
            return str("Gas Station")
        elif "SUPERCENTER" in rows[11] or "WALMART" in rows[11] or "Wal-Mart" in rows[11] or "WAL-MART" in rows[11]:
            return str("Walmart")
        elif "Hulu" in rows[11]:
            return str("Hulu")
        elif "Etsy" in rows[11]:
            return str("Etsy")
        elif "Patreon" in rows[11]:
            return str("Patreon")
        elif "Ortonville" in rows[11]:
            return str("Storage")
        elif "Microsoft" in rows[11]:
            return str("Microsoft")
        elif "UBER " in rows[11] or "Uber" in rows[11] or "UBR" in rows[11]:
            return str("Uber Eats")
        elif "PROG" in rows[11]:
            return str("Car Insurance")
        elif "FUNIMATION" in rows[11]:
            return str("TV")
        elif "SPECTRUM" in rows[11]:
            return str("Internet")
        elif "NINTENDO" in rows[11]:
            return str("Nintendo")
        elif "XCEL" in rows[11]:
            return str("Electricity and Gas")
        elif "FIELD NATION" in rows[11]:
            return str("Field Nation")
        elif "ABCMOUSE" in rows[11]:
            return str("ABCMouse")
        elif "CHASE" in rows[11]:
            return str("Credit card")
        elif "PARAMOUNT" in rows[11]:
            return str("TV")
        elif "Water" in rows[11] or "water" in rows[11]:
            return str("Water")
        elif "AARON" in rows[11]:
            return str("Aarons")
        elif "LEEANN" in rows[11]:
            return str("Leeann Chins")
        elif "SHUTTERFLY" in rows[11]:
            return str("Shutterfly")
        elif "PIZZA HUT" in rows[11]:
            return str("Pizza Hut")
        elif "DOORDASH" in rows[11]:
            return str("DoorDash")
        elif "TREAS" in rows[11]:
            return str("IRS")
        elif "CRICKET" in rows[11]:
            return str("Phones")
        elif "TWITCH" in rows[11]:
            return str("Twitch")
        elif rows[11] == "" and rows[12] != "":
            return str("CashApp")
        else:
            return str("CashApp")



    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Cash.App Reporting Tool')



        #textbox
        self.textbox = QPlainTextEdit(self)
        self.textbox.setReadOnly(True)
        self.textbox.setFont(QFont("Courier New", 10))
        self.textbox.setGeometry(10, 10, 580, 1000)
        self.textbox.setStyleSheet("background-color: #000000; color: #ffffff;")



        #read button
        self.button_read = QPushButton('Run', self)
        self.button_read.setToolTip('Run the program')
        self.button_read.setFont(QFont("Courier New", 10))
        self.button_read.clicked.connect(self.run)



        #scan button
        self.button_scan = QPushButton('Scan', self)
        self.button_scan.setToolTip('Scan the directory')
        self.button_scan.setFont(QFont("Courier New", 10))
        self.button_scan.clicked.connect(self.scan)



        #download button
        self.button_download = QPushButton('Download', self)
        self.button_download.setToolTip('Download the file')
        self.button_download.setFont(QFont("Courier New", 10))
        self.button_download.clicked.connect(self.download)



        #backdate button
        self.button_backdate = QPushButton('Backdate', self)
        self.button_backdate.setToolTip('Backdate the file')
        self.button_backdate.setFont(QFont("Courier New", 10))
        self.button_backdate.clicked.connect(self.backdate)



        #radio buttons
        self.radio_button_1 = QRadioButton('1 Day', self)
        self.radio_button_1.setFont(QFont("Courier New", 10))
        self.radio_button_1.setChecked(True)
        self.radio_button_1.toggled.connect(self.on_radio_button1_toggled)

        self.radio_button_7 = QRadioButton('7 Days', self)
        self.radio_button_7.setFont(QFont("Courier New", 10))
        self.radio_button_7.setChecked(False)
        self.radio_button_7.toggled.connect(self.on_radio_button7_toggled)

        self.radio_button_14 = QRadioButton('14 Days', self)
        self.radio_button_14.setFont(QFont("Courier New", 10))
        self.radio_button_14.setChecked(False)
        self.radio_button_14.toggled.connect(self.on_radio_button14_toggled)

        self.radio_button_30 = QRadioButton('30 Days', self)
        self.radio_button_30.setFont(QFont("Courier New", 10))
        self.radio_button_30.setChecked(False)
        self.radio_button_30.toggled.connect(self.on_radio_button30_toggled)

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.radio_button_1, 1, 1)
        grid.addWidget(self.radio_button_7, 1, 2)
        grid.addWidget(self.radio_button_14, 1, 3)
        grid.addWidget(self.radio_button_30, 1, 4)
        grid.addWidget(self.button_read, 2, 1)
        grid.addWidget(self.button_scan, 2, 2)
        grid.addWidget(self.button_download, 2, 3)
        grid.addWidget(self.button_backdate, 2, 4)
        grid.addWidget(self.textbox, 3, 1, 4, 4)
        self.setLayout(grid)
        self.show()

    def on_radio_button1_toggled(self):
        readery.days = 1
    def on_radio_button7_toggled(self):
        readery.days = 7
    def on_radio_button14_toggled(self):
        readery.days = 14
    def on_radio_button30_toggled(self):
        readery.days = 30
    def run(self):
        self.textbox.clear()
        if self.p is None:  # No process running.
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.start("python", ['readery.py'])
    def scan(self):
        self.textbox.clear()
        if self.p is None:  # No process running.
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.start("python", ['alerting.py'])
    def download(self):
        self.textbox.clear()
        if self.p is None:  # No process running.
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.start("python", ['redownload.py'])
    def backdate(self):
        pass








         
def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = QtWidgets.QMainWindow()
    gui = GUI()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()


























import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "rkd337799!"
)

local = mysql.connector.connect(
    host = "database-1.cdr3vevtjvey.ap-northeast-2.rds.amazonaws.com",
    port = 3306,
    user = "root",
    password = "rkd337799!",
    database = "amrbase"
)
local.close()

from_class = uic.loadUiType("Test7.practice.ui")[0]

class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.btnSearch.clicked.connect(self.Search)
         
       

    def Search(self):
        row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row)
        self.tableWidget.setItem(row, 0, QTableWidgetItem(self.editName.text()))
        self.tableWidget.setItem(row, 1, QTableWidgetItem(self.editGender.text()))
        self.tableWidget.setItem(row, 2, QTableWidgetItem(self.editBirthday.text()))
        self.tableWidget.setItem(row, 3, QTableWidgetItem(self.editAge.text()))
        self.tableWidget.setItem(row, 4, QTableWidgetItem(self.editSex.text()))
        self.tableWidget.setItem(row, 5, QTableWidgetItem(self.editjobtitle.text()))
        self.tableWidget.setItem(row, 6, QTableWidgetItem(self.editAgency.text()))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindows = WindowClass()

    myWindows.show()

    sys.exit(app.exec_())      


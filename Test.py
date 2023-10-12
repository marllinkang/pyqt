# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5 import uic

# push button 사용
# radio button 사용

# from_class = uic.loadUiType("Test.ui")[0]

# class WindowClass(QMainWindow, from_class) :
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         self.setWindowTitle("Test pyQt!")
        
#         self.pushButton_1.clicked.connect(self.button1_Clicked)
#         self.pushButton_2.clicked.connect(self.button2_Clicked)

#         self.radio_1.clicked.connect(self.radio1_Clicked)
#         self.radio_2.clicked.connect(self.radio2_Clicked)
#         self.radio_3.clicked.connect(self.radio3_Clicked)
        
#     def radio1_Clicked(self) :
#         self.textEdit.setText("Radio 1")

#     def radio2_Clicked(self) :
#         self.textEdit.setText("Radio 2")

#     def radio3_Clicked(self) :
#         self.textEdit.setText("Radio 3")
    
#     def button1_Clicked(self) :
#         self.textEdit.setText("Button 1")

#     def button2_Clicked(self) :
#         self.textEdit.setText("Button 2")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     myWindows = WindowClass()

#     myWindows.show()

#     sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic




from_class = uic.loadUiType("Test.ui")[0]

class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Test pyQt!")
        
        self.pushButton_1.clicked.connect(self.button1_Clicked)
        self.pushButton_2.clicked.connect(self.button2_Clicked)

        self.radio_1.clicked.connect(self.radioClicked)
        self.radio_2.clicked.connect(self.radioClicked)
        self.radio_3.clicked.connect(self.radioClicked)
        
    def radioClicked(self) :
       if self.radio_1.isChecked():
           self.textEdit.setText("Radio 1")
       elif self.radio_2.isChecked():
            self.textEdit.setText("Radio 2")
       elif self.radio_3.isChecked():
            self.textEdit.setText("Radio 3")
       else:
            self.textEdit.setText("Unknown")

    
    def button1_Clicked(self) :
        self.textEdit.setText("Button 1")

    def button2_Clicked(self) :
        self.textEdit.setText("Button 2")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindows = WindowClass()

    myWindows.show()

    sys.exit(app.exec_())
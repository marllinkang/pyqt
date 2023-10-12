import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic



from_class = uic.loadUiType("calculator.ui")[0]

class WindowClass(QMainWindow, from_class) :
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("calculator")
        self.value = ""
       
        self.pushButton_0.clicked.connect(self.button0_Clicked)
        self.pushButton_1.clicked.connect(self.button1_Clicked)
        self.pushButton_2.clicked.connect(self.button2_Clicked)
        self.pushButton_3.clicked.connect(self.button3_Clicked)
        self.pushButton_4.clicked.connect(self.button4_Clicked)
        self.pushButton_5.clicked.connect(self.button5_Clicked)
        self.pushButton_6.clicked.connect(self.button6_Clicked)
        self.pushButton_7.clicked.connect(self.button7_Clicked)
        self.pushButton_8.clicked.connect(self.button8_Clicked)
        self.pushButton_9.clicked.connect(self.button9_Clicked)
        self.pushButton_10.clicked.connect(self.button10_delete_Clicked)
        self.pushButton_11.clicked.connect(self.button11_Clicked)
        self.pushButton_12.clicked.connect(self.button12_Clicked)
        self.pushButton_13.clicked.connect(self.button13_Clicked)
        self.pushButton_14.clicked.connect(self.button14_Clicked)
        self.pushButton_15.clicked.connect(self.button15_Clicked)
        self.pushButton_16.clicked.connect(self.button16_Clicked)
        self.pushButton_17.clicked.connect(self.button17_Clicked)
        self.pushButton_18.clicked.connect(self.button18_Clicked)
        self.pushButton_19.clicked.connect(self.button19_Clicked)

    
    def number(self,num):
        exit_text = self.textEdit.setText()
        self.textEdit.setText(exit_text + num)

    def button0_Clicked(self):
        self.value += '0'
        self.textEdit.setText(self.value)
        # self.number("0")
    
    def button1_Clicked(self):
        self.value += '1'
        self.textEdit.setText(self.value)

    def button2_Clicked(self):
        self.value += '2'
        self.textEdit.setText(self.value)

    def button3_Clicked(self):
        self.value += '3'
        self.textEdit.setText(self.value)

    def button4_Clicked(self):
        self.value += '4'
        self.textEdit.setText(self.value)

    def button5_Clicked(self):
        self.value += '5'
        self.textEdit.setText(self.value)

    def button6_Clicked(self):
        self.value += '6'
        self.textEdit.setText(self.value)

    def button7_Clicked(self):
        self.value += '7'
        self.textEdit.setText(self.value)

    def button8_Clicked(self):
        self.value += '8'
        self.textEdit.setText(self.value)
    
    def button9_Clicked(self):
        self.value += '9'
        self.textEdit.setText(self.value)

    # 가장 끝의 값만 삭제

    def button10_delete_Clicked(self):
        self.value = self.textEdit.toPlainText()
        new_value = self.value[:-1]
        self.textEdit.setText(new_value)
      
    
    def button11_Clicked(self):
        self.value += '+/-' 
        self.textEdit.setText(self.value)
   
    def button12_Clicked(self):
        self.value += '%'
        self.textEdit.setText(self.value)
        
    def button13_Clicked(self):
        self.value += '/'
        self.textEdit.setText(self.value)

    def button14_Clicked(self):
        self.value += '*'
        self.textEdit.setText(self.value)

    def button15_Clicked(self):
        self.value += '-'
        self.textEdit.setText(self.value)

    def button16_Clicked(self):
        self.value += '+'
        self.textEdit.setText(self.value)

    def button17_Clicked(self):
        self.value += '.'
        self.textEdit.setText(self.value)

    # 결과
    
    
    def button18_Clicked(self):
        if self.value:
            try:
              result = eval(self.value)  # 입력된 수식 계산
              self.textEdit_2.setText(self.value + " = " + str(result))  # 결과를 텍스트 상자에 표시
            except Exception as e:
                self.textEdit.setText(e)
        else:
            self.textEdit.setText("0")



# 계산기 리셋 함수
    def button19_Clicked(self):
        self.textEdit.setText(" ")
        self.value = self.textEdit.toPlainText()
        new_value = self.value
        self.textEdit.setText(new_value)
        
   
    def write(self):
        self.label.setText(self.lineEdit.text())   
    
   

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindows = WindowClass()

    myWindows.show()

    sys.exit(app.exec_())
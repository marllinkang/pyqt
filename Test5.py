import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic


# from_class = uic.loadUiType("Test5.ui")[0]

# class WindowClass(QMainWindow, from_class) :
    
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)

#         self.btnInput.clicked.connect(self.inputName)

#     def inputName(self):
#         text, ok = QInputDialog.getText(self, 'QInputDialog - Name','User name:')


#         if ok and text:
#             self.textEdit.append(text)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     myWindows = WindowClass()

#     myWindows.show()

#     sys.exit(app.exec_())       

# from_class = uic.loadUiType("Test5.ui")[0]

# class WindowClass(QMainWindow, from_class) :
    
#     def __init__(self):
#         super().__init__()                                             
#         self.setupUi(self)

#         self.btnName.clicked.connect(self.inputName)
#         self.btnSeason.clicked.connect(self.inputSeason)
    
#     def inputSeason(self):
#         items = ['spring', 'summer', 'Fall', 'Winter'] # 4가지를 선택 할 수 있다.
#         item, ok = QInputDialog.getItem(self, 'QInputDialog - season','season:', items,  0, False)

#         if ok and item:
#             self.textEdit.append(item)

#     def inputName(self):
#         text, ok = QInputDialog.getText(self, 'QInputDialog - Name','User name:')


#         if ok and text:
#             self.textEdit.append(text)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     myWindows = WindowClass()

#     myWindows.show()

#     sys.exit(app.exec_())      


# 2 ColorDialog
# 폰트 색상 변경

# from_class = uic.loadUiType("Test5.ui")[0]

# class WindowClass(QMainWindow, from_class) :
    
#     def __init__(self):
#         super().__init__()                                             
#         self.setupUi(self)

#         self.btnName.clicked.connect(self.inputName)
#         self.btnSeason.clicked.connect(self.inputSeason)
#         self.btncolor.clicked.connect(self.inputColor)
    
#     def inputColor(self):
#         color = QColorDialog.getColor()
    
#         if color.isValid():
#             self.textEdit.append("Color")
#             self.textEdit.selectAll()
#             self.textEdit.setTextColor(color)
#             self.textEdit.moveCursor(QTextCursor.End)

#     def inputSeason(self):
#         items = ['spring', 'summer', 'Fall', 'Winter'] # 4가지를 선택 할 수 있다.
#         item, ok = QInputDialog.getItem(self, 'QInputDialog - season','season:', items,  0, False)

#         if ok and item:
#             self.textEdit.append(item)

#     def inputName(self):
#         text, ok = QInputDialog.getText(self, 'QInputDialog - Name','User name:')


#         if ok and text:
#             self.textEdit.append(text)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     myWindows = WindowClass()

#     myWindows.show()

#     sys.exit(app.exec_())      

# 3 FontDialog
# from_class = uic.loadUiType("Test5.ui")[0]

# class WindowClass(QMainWindow, from_class) :
    
#     def __init__(self):
#         super().__init__()                                             
#         self.setupUi(self)

#         self.btnName.clicked.connect(self.inputName)
#         self.btnSeason.clicked.connect(self.inputSeason)
#         self.btncolor.clicked.connect(self.inputColor)
#         self.btnFont.clicked.connect(self.inputFont)
#     def inputFont(self):
#         font, ok =QFontDialog.getFont()

#         if ok and font:
#             info = QFontInfo(font)
#             self.textEdit.append(info.family() + info.styleName())
#             self.textEdit.selectAll()
#             self.textEdit.setFont(font)
#             self.textEdit.moveCursor(QTextCursor.End)

#     def inputColor(self):
#         color = QColorDialog.getColor()
    
#         if color.isValid():
#             self.textEdit.append("Color")
#             self.textEdit.selectAll()
#             self.textEdit.setTextColor(color)
#             self.textEdit.moveCursor(QTextCursor.End)

#     def inputSeason(self):
#         items = ['spring', 'summer', 'Fall', 'Winter'] # 4가지를 선택 할 수 있다.
#         item, ok = QInputDialog.getItem(self, 'QInputDialog - season','season:', items,  0, False)

#         if ok and item:
#             self.textEdit.append(item)

#     def inputName(self):
#         text, ok = QInputDialog.getText(self, 'QInputDialog - Name','User name:')


#         if ok and text:
#             self.textEdit.append(text)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     myWindows = WindowClass()

#     myWindows.show()

#     sys.exit(app.exec_())      

# 4 FileDialog
# 파일 찾기
# from_class = uic.loadUiType("Test5.ui")[0]

# class WindowClass(QMainWindow, from_class) :
    
#     def __init__(self):
#         super().__init__()                                             
#         self.setupUi(self)

#         self.btnName.clicked.connect(self.inputName)
#         self.btnSeason.clicked.connect(self.inputSeason)
#         self.btncolor.clicked.connect(self.inputColor)
#         self.btnFont.clicked.connect(self.inputFont)
#         self.btnfile.clicked.connect(self.inputfile)
    
#     def inputfile(self):
#         name = QFileDialog.getOpenFileName(self, 'open File', './')

#         if name[0]:
#             with open(name[0], 'r') as file:
#                 data = file.read()
#                 self.textEdit.setText(data)

#     def inputFont(self):
#         font, ok =QFontDialog.getFont()

#         if ok and font:
#             info = QFontInfo(font)
#             self.textEdit.append(info.family() + info.styleName())
#             self.textEdit.selectAll()
#             self.textEdit.setFont(font)
#             self.textEdit.moveCursor(QTextCursor.End)
            
#     def inputColor(self):
#         color = QColorDialog.getColor()
    
#         if color.isValid():
#             self.textEdit.append("Color")
#             self.textEdit.selectAll()
#             self.textEdit.setTextColor(color)
#             self.textEdit.moveCursor(QTextCursor.End)

#     def inputSeason(self):
#         items = ['spring', 'summer', 'Fall', 'Winter'] # 4가지를 선택 할 수 있다.
#         item, ok = QInputDialog.getItem(self, 'QInputDialog - season','season:', items,  0, False)

#         if ok and item:
#             self.textEdit.append(item)

#     def inputName(self):
#         text, ok = QInputDialog.getText(self, 'QInputDialog - Name','User name:')


#         if ok and text:
#             self.textEdit.append(text)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     myWindows = WindowClass()

#     myWindows.show()

#     sys.exit(app.exec_())      

# 5 MessageDialog

# 5.1 QMessageDialog

# from_class = uic.loadUiType("Test5.ui")[0]

# class WindowClass(QMainWindow, from_class) :
    
#     def __init__(self):
#         super().__init__()                                             
#         self.setupUi(self)

#         self.btnName.clicked.connect(self.inputName)
#         self.btnSeason.clicked.connect(self.inputSeason)
#         self.btncolor.clicked.connect(self.inputColor)
#         self.btnFont.clicked.connect(self.inputFont)
#         self.btnfile.clicked.connect(self.inputfile)
    
#     def inputfile(self):
#         name = QFileDialog.getOpenFileName(self, 'open File', './')

#         if name[0]:
#             with open(name[0], 'r') as file:
#                 data = file.read()
#                 self.textEdit.setText(data)
                
#     def inputFont(self):
#         font, ok =QFontDialog.getFont()

#         if ok and font:
#             info = QFontInfo(font)
#             self.textEdit.append(info.family() + info.styleName())
#             self.textEdit.selectAll()
#             self.textEdit.setFont(font)
#             self.textEdit.moveCursor(QTextCursor.End)
#             # 5.3 코드 추가
#             # LineEdit 에 텍스트를 입력하고 엔터를 누르면, 입력이 숫자인지 체크
#             # 숫자라면 TextEdit 에 출력하고 숫자가 아니라면 MessageBox 를 띄워 경고하고 입력한 텍스트를 지워준다.
#             self.lineEdit.returnPressed.connect(self.inputNumber)

#     def inputNumber(self):
#         text = self.lineEdit.text()

#         if text.isdigit():
#             self.textEdit.setText(text)
#         else:
#             QMessageBox.warning(self, 'QMessagebox - setText', 'Please enter only numbers.')
#             self.lineEdit.clear()

#     def inputColor(self):
#         color = QColorDialog.getColor()
    
#         if color.isValid():
#             self.textEdit.append("Color")
#             self.textEdit.selectAll()
#             self.textEdit.setTextColor(color)
#             self.textEdit.moveCursor(QTextCursor.End)

#     def inputSeason(self):
#         items = ['spring', 'summer', 'Fall', 'Winter'] # 4가지를 선택 할 수 있다.
#         item, ok = QInputDialog.getItem(self, 'QInputDialog - season','season:', items,  0, False)

#         if ok and item:
#             self.textEdit.append(item)

#     def inputName(self):
#         text, ok = QInputDialog.getText(self, 'QInputDialog - Name','User name:')


#         if ok and text:
#             self.textEdit.append(text)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     myWindows = WindowClass()

#     myWindows.show()

#     sys.exit(app.exec_())  

# 숫자가 아니라면 그냥 출근할지 다시 입력할지 물어보도록 수정    

from_class = uic.loadUiType("Test5.ui")[0]

class WindowClass(QMainWindow, from_class) :
    
    def __init__(self):
        super().__init__()                                             
        self.setupUi(self)

        self.btnName.clicked.connect(self.inputName)
        self.btnSeason.clicked.connect(self.inputSeason)
        self.btncolor.clicked.connect(self.inputColor)
        self.btnFont.clicked.connect(self.inputFont)
        self.btnfile.clicked.connect(self.inputfile)
        self.lineEdit.returnPressed.connect(self.question)
    def question(self):
        text = self.lineEdit.text()

        if text.isdigit():
            self.textEdit.settext(text)
        else:
            retval = QMessageBox.question(self, 'QMessageBox -qustion','Are you sure printf?', QMessageBox.Yes| QMessageBox.No,QMessageBox.No) #NO, YES의 칸의 색이 다르다
        if retval == QMessageBox.Yes:
            self.TextEdit.setText(text)
        else:
            self.lineEdit.clear()

    def inputfile(self):
        name = QFileDialog.getOpenFileName(self, 'open File', './')

        if name[0]:
            with open(name[0], 'r') as file:
                data = file.read()
                self.textEdit.setText(data)
                
    def inputFont(self):
        font, ok =QFontDialog.getFont()

        if ok and font:
            info = QFontInfo(font)
            self.textEdit.append(info.family() + info.styleName())
            self.textEdit.selectAll()
            self.textEdit.setFont(font)
            self.textEdit.moveCursor(QTextCursor.End)
            # 5.3 코드 추가
            # LineEdit 에 텍스트를 입력하고 엔터를 누르면, 입력이 숫자인지 체크
            # 숫자라면 TextEdit 에 출력하고 숫자가 아니라면 MessageBox 를 띄워 경고하고 입력한 텍스트를 지워준다.
            self.lineEdit.returnPressed.connect(self.inputNumber)

    def inputNumber(self):
        text = self.lineEdit.text()

        if text.isdigit():
            self.textEdit.setText(text)
        else:
            QMessageBox.warning(self, 'QMessagebox - setText', 'Please enter only numbers.')
            self.lineEdit.clear()

    def inputColor(self):
        color = QColorDialog.getColor()
    
        if color.isValid():
            self.textEdit.append("Color")
            self.textEdit.selectAll()
            self.textEdit.setTextColor(color)
            self.textEdit.moveCursor(QTextCursor.End)

    def inputSeason(self):
        items = ['spring', 'summer', 'Fall', 'Winter'] # 4가지를 선택 할 수 있다.
        item, ok = QInputDialog.getItem(self, 'QInputDialog - season','season:', items,  0, False)

        if ok and item:
            self.textEdit.append(item)

    def inputName(self):
        text, ok = QInputDialog.getText(self, 'QInputDialog - Name','User name:')


        if ok and text:
            self.textEdit.append(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindows = WindowClass()

    myWindows.show()

    sys.exit(app.exec_())      






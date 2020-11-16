import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
from_class = uic.loadUiType("textBrowser.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_Print.clicked.connect(self.printTextFunction)
        self.btn_SetText.clicked.connect(self.changeTextFunction)
        self.btn_AppendText.clicked.connect(self.appendTextFunction)
        self.btn_Clear.clicked.connect(self.clearTextFunction)

    def printTextFunction(self):
        # self.Textbrowser이름.toPlainText()
        # Textbrowser에 있는 글자를 가져오는 메서드
        print(self.textbrow_Test.toPlainText())

    def changeTextFunction(self):
        # self.Textbrowser이름.setPlainText()
        # Textbrowser에 새롭게 글자를 작성하는 메서드
        self.textbrow_Test.setPlainText("This is Textbrowser - Change Text")

    def appendTextFunction(self):
        # self.Textbrowser이름.append()
        # Textbrowser에 글자를 추가하는 메서드
        self.textbrow_Test.append("Append Text")

    def clearTextFunction(self):
        # self.Textbrowser.clear()
        # Textbrowser에 있는 글자를 지우는 메서드
        self.textbrow_Test.clear()

if __name__ =="__main__":
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
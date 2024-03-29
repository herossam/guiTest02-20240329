import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic # qt designer에서 제작한 ui를 불어오는 클릭

form_class = uic.loadUiType("ui/test.ui")[0] # Qt Designer에서 만듣 ui를 불러옴

class MyWindow(QMainWindow,):
    def __init__(self):
        super().__init__() # 부모 클래스 생성자 호출
        self.setupUi(self) # 위에서 불러온 test.ui를 연결
        self.setWindowTitle()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from winform import *
import tsclib

class win(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        # 初始化界面
        super(win, self).__init__(parent)
        self.setupUi(self)
        # 关联信号和槽
        self.btnPrint.clicked.connect(self.printSample)

    def printSample(self):
        # 打印标签
        self.initPrinter()
        if self.radBtn1.isChecked():
            print("项目一")
        if self.radBtn2.isChecked():
            print("项目二")
        if self.radBtn3.isChecked():
            print("项目三")
        if self.radBtn4.isChecked():
            print("项目四")
        if self.radBtn5.isChecked():
            print("项目5")
        if self.radBtn6.isChecked():
            print(("项目六"))
        tsclib.closePrinter()

    def initPrinter(self):
        # 初始化打印机
        tsclib.openPrinter("TSC TTP-244M Pro")
        tsclib.setupPrinter(40, 20, 1.0, 8, 0, 2, 0)
        tsclib.sendCommand("DIRECTION 1".encode("gbk"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = win()
    mainWin.show()
    sys.exit(app.exec())
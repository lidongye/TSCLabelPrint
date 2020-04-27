import sys
from datetime import date
from PyQt5.QtWidgets import QApplication, QMainWindow
from winform import *
import tsclib

class win(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        # 初始化界面
        super(win, self).__init__(parent)
        self.setupUi(self)
        self.radBtn1.setChecked(True)
        # 关联信号和槽
        self.btnPrint.clicked.connect(self.printSample)

    def printSample(self):
        # 设置打印项目
        testNum = 0
        testList = [["HIV、RPR、TPPA"], ["HIV（复）"], ["HIV（复）", "EDTA（留）"], ["HIV、RPR、TPPA"], ["十三五亲和力"],
                    ["HIV（复）", "EDTA(CD4)"]]
        strDate = date.today().isoformat()
        if self.radBtn1.isChecked():
            testNum = 0
        if self.radBtn2.isChecked():
            testNum = 1
        if self.radBtn3.isChecked():
            testNum = 2
        if self.radBtn4.isChecked():
            testNum = 3
        if self.radBtn5.isChecked():
            testNum = 4
        if self.radBtn6.isChecked():
            testNum = 5
        tests = testList[testNum]
        self.initPrinter()
        for test in tests:
            tsclib.clearBuffer()
            tsclib.windowsFont(10, 10, 40, 0, 0, 0, "宋体", "姓名：{}".format(self.edtName.text()))
            tsclib.windowsFont(10, 60, 25, 0, 0, 0, "宋体", "项目：{}".format(test))
            if testNum == 3:
                tsclib.windowsFont(10, 90, 25, 0, 0, 0, "宋体", "十三五横断面")
            tsclib.windowsFont(10, 120, 25, 0, 0, 0, "宋体", "采集时间：{}".format(strDate))
            if testNum == 4:
                tsclib.printLabel(1 , 4)
            else:
                tsclib.printLabel(1, 1)
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
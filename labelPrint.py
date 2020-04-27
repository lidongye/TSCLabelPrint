from winform import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class win(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(win, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = win()
    mainWin.show()
    sys.exit(app.exec())
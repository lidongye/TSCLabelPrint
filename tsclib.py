'''
使用ctypes调用TSCLIB.dll，重新封装
'''
import ctypes

tsclib = ctypes.WinDLL(r"./tsclib/TSCLIB.dll")

def openPrinter(ptrName):
    '''
    打开打印机的端口
    :param ptrName:打印机名称，字符串型，如"TSC TTP-244M Pro"。
    :return:无
    '''
    tsclib.openport(ptrName)

def closePrinter():
    '''
    关闭打印机的端口。
    :return: 无
    '''
    tsclib.closeport()

def clearBuffer():
    '''
    清除打印机缓存
    :return: 无
    '''
    tsclib.clearbuffer()

def barCode(X, Y, barType, barH, barText, barDegree, width, narrow, content):
    '''
    使用打印机内部编码打印条形码。
    :param X: 字符串型，X方向起点
    :param Y: 字符串型，Y方向起点
    :param barType: 字符串型，条形码类别："128", "128M", "EAN128", "25", "25C", "39", "39C",
                    "93", "EAN13", "EAN13+2", "EAN13+5", "EAN8", "EAN8+2", "EAN8+5", "CODA",
                    "POST", "UPCA", "UPCA+2", "UPCA+5", "UPCE", "UPCE+2", "UPCE+5"
    :param barH: 字符串型，条形码高度
    :param barText: 字符串型，是否打印条码码文，"0"：不打印，"1"：打印
    :param barDegree: 字符串型，条形码旋转角度，"0":不旋转，"90"：旋转90度，"180"：旋转180度，"270":旋转270度
    :param width: 字符串型，设定条形码宽比例因子，参考TSPL手册
    :param narrow: 字符串型， 设定条形码窄比例因子，参考TSPL手册
    :param content: 字符串型，条形码内容
    :return:
    '''
    tsclib.barcode(X, Y, barType, barH, barText, barDegree, width, narrow, content)

'''
使用ctypes调用TSCLIB.dll，重新封装
'''
import ctypes

tsclib = ctypes.WinDLL(r"./tsclib/TSCLIB.dll")

def openPrinter(prtName):
    '''
    打开打印机的端口
    :param prtName:打印机名称，字符串型，如"TSC TTP-244M Pro"。
    :return:无
    '''
    tsclib.openport(prtName.encode("gbk"))  # 打印机不接受UTF-8字符串

def closePrinter():
    '''
    关闭打印机的端口。
    :return: 无
    '''
    tsclib.closeport()

def setupPrinter(labelW, labelH, speed, darkness, sensor, gap, offset):
    '''
    设置标签宽度，高度，打印速度，打印浓度，传感器类别，标签垂直间距，偏移距离。
    :param labelW:字符串型，标签宽度，单位mm
    :param labelH:字符串型，标签高度，单位mm
    :param speed:字符串型，打印速度，"1.0"，"1.5"，"2.0"，"3.0"，"4.0"，"6.0"，"8.0"，"10.0"寸/秒
    :param darkness:字符串型，打印浓度，"0"~"15"
    :param sensor:字符串型，传感器类别，"0"：垂直间距传感器，"1"：黑标检测传感器
    :param gap:字符串型，垂直间距，单位mm
    :param offset:字符串型，偏移距离，单位mm，一般标签为"0"
    :return:
    '''
    tsclib.setup(str(labelW).encode("gbk"), str(labelH).encode("gbk"), str(speed).encode("gbk"), str(darkness).encode("gbk"), str(sensor).encode("gbk"), str(gap).encode("gbk"), str(offset).encode("gbk"))  # 为调用方便转成字符串型

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
    tsclib.barcode(str(X).encode("gbk"), str(Y).encode("gbk"), barType.encode("gbk"), str(barH).encode("gbk"), str(barText).encode("gbk"), str(barDegree).encode("gbk"), str(width).encode("gbk"), str(narrow).encode("gbk"), content.encode("gbk"))

def printFont(X, Y, fontName, degree, scaleX, scaleY, content):
    '''
    使用打印机内部字库打印文字
    :param X: 字符串型， X方向起点
    :param Y: 字符串型，Y方向起点
    :param fontName:字符串型，内部字库名称：1: 8*/12 dots
                                        2: 12*20 dots
                                        3: 16*24 dots
                                        4: 24*32 dots
                                        5: 32*48 dots
                                        TST24.BF2: 繁体中文24*24
                                        TST16.BF2: 繁体中文16*16
                                        TTT24.BF2: 繁体中文24*24 (电信码)
                                        TSS24.BF2: 简体中文24*24
                                        TSS16.BF2: 简体中文16*16
                                        K: 韩文24*24
                                        L: 韩文16*16
    :param degree:字符串型，旋转角度，"0":不旋转，"90"：旋转90度，"180"：旋转180度，"270":旋转270度
    :param scaleX:字符串型，X方向放大倍数，"1"~"8"
    :param scaleY:字符串型，Y方向放大倍数，"1"~"8"
    :param content:字符串型，文字内容
    :return:无
    '''
    tsclib.printerfont(str(X).encode("gbk"), str(Y).encode("gbk"), fontName.encode("gbk"), str(degree).encode("gbk"), str(scaleX).encode("gbk"), str(scaleY).encode("gbk"), content.encode("gbk"))

def sendCommand(command):
    '''
    发送指令到打印机
    :param command: 字符串型，指令参考TSPL
    :return: 无
    '''
    tsclib.sendcommand(command)

def printLabel(setsNum, copiesNum):
    '''
    打印标签
    :param setsNum:字符串型，打印式数
    :param copiesNum: 字符串型，打印份数
    :return: 无
    '''
    tsclib.printlabel(str(setsNum), str(copiesNum))  # 为调用方便，转成字符串

def downloadPcx(filePath, fileName):
    '''
    下载单色PCX格式图片至打印机
    :param filePath: 字符串型，文件路径
    :param fileName: 字符串型，下载到打印机内的名称（使用大写英文）
    :return: 无
    '''
    tsclib.downloadpcx(filePath, fileName)

def formFeed():
    '''
    跳页，须在setup后使用
    :return: 无
    '''
    tsclib.formfeed()

def nobackFeed():
    '''
    设置纸张不回吐
    :return: 无
    '''
    tsclib.nobackfeed()

def windowsFont(X, Y, fontH, degree, fontStyle, underline, fontName, content):
    '''
    使用Windows TTF字体打印文字
    :param X: 整数型，X方向起点
    :param Y: 整数型Y方向起点
    :param fontH:整数型，字体高度
    :param degree: 整数型，旋转角度，0:不旋转，90：旋转90度，180：旋转180度，270:旋转270度
    :param fontStyle: 整数型，字形， 0：标准，1：倾斜，2，加粗，3：加粗倾斜
    :param underline: 整数型，下划线，0：无下划线，1：有下划线
    :param fontName: 字符串型，字体名称，如"宋体"
    :param content: 字符串型，打印内容
    :return: 无
    '''
    tsclib.windowsfont(X, Y, fontH, degree, fontStyle, underline, fontName.encode("gbk"), content.encode("gbk"))

def about():
    '''
    显示DLL版本号
    :return: 无
    '''
    tsclib.about()

def sendBinaryData(binData, binLen):
    '''
    传送二进制数据
    :param binData:二进制数据
    :param binLen: 整数型，数据长度
    :return:
    '''
    tsclib.sendBinaryData(binData, binLen)

def windowsFontUnicode(X, Y, fontH, degree, fontStyle, underline, fontName, binData):
    '''
    使用Windows TTF字体打印Unicode文字
    :param X: 整数型，X方向起点
    :param Y: 整数型Y方向起点
    :param fontH: 整数型，字体高度
    :param degree: 整数型，旋转角度，0:不旋转，90：旋转90度，180：旋转180度，270:旋转270度
    :param fontStyle: 整数型，字形， 0：标准，1：倾斜，2，加粗，3：加粗倾斜
    :param underline: 整数型，下划线，0：无下划线，1：有下划线
    :param fontName: 字符串型，字体名称，如"宋体"
    :param binData: 二进制数据
    :return: 无
    '''
    tsclib.wondowsfontUnicode(X, Y, fontH, degree, fontStyle, underline, fontName, binData)

def usbportQuery():
    '''
    从usb接口查询打印机状态，参考TSPL手册中的<ESC>!?指令
    :return:
    '''
    tsclib.usbportqueryprinter()

def usbprinterName():
    '''
    从usb接口返回打印机名称
    :return:
    '''
    tsclib.usbprintername()

def usbprinterSerial():
    '''
    从usb接口返回打印机序号
    :return:
    '''
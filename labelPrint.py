import tsclib
# 测试
# 初始化打印机
tsclib.openPrinter("TSC TTP-244M Pro")
tsclib.setupPrinter(40, 20, 1.0, 8, 0, 2, 0)
# tsclib.sendCommand("SIZE 40 mm, 20 mm".encode("gbk"))  # 设置纸张大小
# tsclib.sendCommand("GAP 2mm, 0mm".encode("gbk"))  # 设置标签间距
tsclib.sendCommand("DIRECTION 1".encode("gbk"))  # 设置打印方向
tsclib.clearBuffer()
# tsclib.windowsFont(20, 20, 40, 0, 0, 0, "宋体", "甄吴廖ABC")
# tsclib.printFont(20, 20, "TSS24.BF2", 0, 1, 1, "甄吴廖")
# tsclib.barCode(10, 10, "128", 35, 1, 0, 2, 2, "1234567890abcd")
tsclib.printLabel(1, 1)
tsclib.closePrinter()
'''
使用ctypes调用TSCLIB.dll，重新封装
'''
import ctypes

tsclib = ctypes.WinDLL(r"./tsclib/TSCLIB.dll")

def openPrinter(ptrName):
    tsclib.openport(ptrName)

def closePrinter():
    tsclib.closeport()

def sendCommand(command):
    tsclib.sendcommand(command)

def


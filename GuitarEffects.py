import numpy as np
import wavio
import WavUtils as util
import wx
from Gui import *


if __name__ == '__main__':
    mainApp = wx.App()
    mainFrame = MainWindow(parent = None, id = -1) 
    mainFrame.Show()       
    mainApp.MainLoop()
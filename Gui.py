import wx
import tkinter as tk
from tkinter import filedialog
import WavUtils as util

class MainWindow(wx.Frame):

    def __init__(self, parent, id):
        # Create main window and add basic functionality
        wx.Frame.__init__(self, parent, id, 'Guitar Effects', size = (600, 400))
        mainPanel = wx.Panel(self)
        self.Bind(wx.EVT_CLOSE, self.closewindow)

        # Menu bar
        menuBar = wx.MenuBar()

        # 'File' menu
        fileMenu = wx.Menu()

        # File/Open
        fileOpen = fileMenu.Append(wx.ID_NEW, "Open")
        self.Bind(wx.EVT_MENU, self.openfile, fileOpen)

        # File/Exit
        fileExit = fileMenu.Append(wx.ID_EXIT, "Exit")
        self.Bind(wx.EVT_MENU, self.closewindow, fileExit)

        menuBar.Append(fileMenu, 'File')

        self.SetMenuBar(menuBar)


    def closewindow(self, event):
        """Close a window"""
        self.Destroy()

    def openfile(self, event):

        root = tk.Tk()
        root.withdraw()

        dialogTitle = "Select a .wav file"
        ftypes = [("WAV", ".wav")]

        filepath = filedialog.askopenfilename(initialdir = "./", title = dialogTitle, filetypes = ftypes)

        root.destroy()
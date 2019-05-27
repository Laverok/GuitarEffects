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

        ### Menu bar
        menuBar = wx.MenuBar()

        # 'File' menu
        fileMenu = wx.Menu()

        # File/Open
        fileOpen = fileMenu.Append(wx.ID_NEW, "Open")
        self.Bind(wx.EVT_MENU, self.openfile, fileOpen)

        # File/Save
        fileSave = fileMenu.Append(wx.ID_NEW, "Save as")
        self.Bind(wx.EVT_MENU, self.savefile, fileSave)

        # File/Exit
        fileExit = fileMenu.Append(wx.ID_EXIT, "Exit")
        self.Bind(wx.EVT_MENU, self.closewindow, fileExit)

        menuBar.Append(fileMenu, 'File')
        self.SetMenuBar(menuBar)
        
        # Status boxes
        boxWidth = 100
        boxHeight = 320
        boxSize = (boxWidth, boxHeight)

        initialWidth = 1
        initialHeight = 0
        pos0 = (initialWidth, initialHeight)
        pos1 = (initialWidth + boxWidth, initialHeight)
        pos2 = (initialWidth + 2*boxWidth, initialHeight)
        pos3 = (initialWidth + 3*boxWidth, initialHeight)
        pos4 = (initialWidth + 4*boxWidth, initialHeight)

        playBox = wx.StaticBox(mainPanel, wx.ID_NEW, "Play", pos = pos0, size = boxSize )
        echoBox = wx.StaticBox(mainPanel, wx.ID_NEW, "Echo", pos = pos1, size = boxSize )
        distBox = wx.StaticBox(mainPanel, wx.ID_NEW, "Distortion", pos = pos2, size = boxSize )
        temp1Box = wx.StaticBox(mainPanel, wx.ID_NEW, "Effect no. 3", pos = pos3, size = boxSize )
        temp2Box = wx.StaticBox(mainPanel, wx.ID_NEW, "Effect no. 4", pos = pos4, size = boxSize )

        # Buttons
        buttonSize = (boxWidth, boxWidth / 2)
        playOrigButton = wx.Button(mainPanel, wx.ID_NEW, "Play original", pos = (0, 20), size = buttonSize)
        playModiButton = wx.Button(mainPanel, wx.ID_NEW, "Play modified", pos = (0, 70), size = buttonSize)

        # Text boxes
        
    
    
    def closewindow(self, event):
        """Close a window"""
        self.Destroy()


    def openfile(self, event):
        """"Open a file"""
        root = tk.Tk()
        root.withdraw()

        dialogTitle = "Select a file"
        ftypes = [("WAV", ".wav")]

        filepath = filedialog.askopenfilename(initialdir = "./", title = dialogTitle, filetypes = ftypes)

        root.destroy()

    def savefile(self, event):
        """Save a file"""

        root = tk.Tk()
        root.withdraw()

        dialogTitle = "Select a file"
        ftypes = [("WAV", ".wav")]

        filepath = filedialog.asksaveasfilename(initialdir = "./", title = dialogTitle, filetypes = ftypes)
import wx
import tkinter as tk
from tkinter import filedialog
from WavUtils import *
from WavInterface import *


class MainWindow(wx.Frame):
    """Class representing main window of the app
       Derived from wx.Frame
    """


    def __init__(self, parent, id):

        # Initialize an interface which is the engine of the app
        self.wavInterface = WavInterface()

        # Create main window and add basic functionality
        wx.Frame.__init__(self, parent, id, 'Guitar Effects', size = (640, 480))
        mainPanel = wx.Panel(self)
        self.Bind(wx.EVT_CLOSE, self.closewindow)

        ### Menu bar
        menuBar = wx.MenuBar()

        # 'File' menu
        fileMenu = wx.Menu()

        # File/Open
        fileOpen = fileMenu.Append(wx.ID_ANY, "Open")
        self.Bind(wx.EVT_MENU, self.openfile, fileOpen)

        # File/Save
        fileSave = fileMenu.Append(wx.ID_ANY, "Save as")
        self.Bind(wx.EVT_MENU, self.savefile, fileSave)

        # File/Exit
        fileExit = fileMenu.Append(wx.ID_EXIT, "Exit")
        self.Bind(wx.EVT_MENU, self.closewindow, fileExit)

        menuBar.Append(fileMenu, 'File')
        self.SetMenuBar(menuBar)
        
        # Status boxes
        boxWidth = 120
        boxHeight = 400
        boxSize = (boxWidth, boxHeight)

        initialWidth = 1
        initialHeight = 0
        pos0 = (initialWidth, initialHeight)
        pos1 = (initialWidth + boxWidth, initialHeight)
        pos2 = (initialWidth + 2*boxWidth, initialHeight)
        pos3 = (initialWidth + 3*boxWidth, initialHeight)
        pos4 = (initialWidth + 4*boxWidth, initialHeight)
        pos5 = (initialWidth, initialHeight + boxHeight/2)

        playBox = wx.StaticBox(mainPanel, wx.ID_ANY, "Play", pos = pos0, size = (boxWidth, boxHeight/2) )
        echoBox = wx.StaticBox(mainPanel, wx.ID_ANY, "Echo", pos = pos1, size = boxSize )
        distBox = wx.StaticBox(mainPanel, wx.ID_ANY, "Distortion", pos = pos2, size = boxSize )
        temp1Box = wx.StaticBox(mainPanel, wx.ID_ANY, "Effect no. 3", pos = pos3, size = boxSize )
        temp2Box = wx.StaticBox(mainPanel, wx.ID_ANY, "Effect no. 4", pos = pos4, size = boxSize )
        applyBox = wx.StaticBox(mainPanel, wx.ID_ANY, "Apply effects", pos = pos5, size = (boxWidth, boxHeight/2) )

        # Play box
        buttonSize = (boxWidth, boxWidth / 2)
        playOrigButton = wx.Button(mainPanel, wx.ID_ANY, "Play original", pos = (0, 30), size = buttonSize)
        playModiButton = wx.Button(mainPanel, wx.ID_ANY, "Play modified", pos = (0, 120), size = buttonSize)

        # Echo box
        textSize = (50, 20)

        echoCheck = wx.CheckBox(mainPanel, wx.ID_ANY, "Apply", pos = (130, 30))

        wx.StaticText(mainPanel, wx.ID_ANY, "Delay [s]", pos = (130, 60))
        echoDelayInput = wx.TextCtrl(mainPanel, wx.ID_ANY, pos = (130, 80), size = textSize)

        wx.StaticText(mainPanel, wx.ID_ANY, "Decay factor (0-1)", pos = (130, 110))
        echoDecayInput = wx.TextCtrl(mainPanel, wx.ID_ANY, pos = (130, 130), size = textSize)
        
        # Distortion box
        distCheck = wx.CheckBox(mainPanel, wx.ID_ANY, "Apply", pos = (250, 30))

        wx.StaticText(mainPanel, wx.ID_ANY, "Input gain (>1)", pos = (250, 60))
        echoDelayInput = wx.TextCtrl(mainPanel, wx.ID_ANY, pos = (250, 80), size = textSize)

        # Apply effects box
        applyButton = wx.Button(mainPanel, wx.ID_ANY, "Apply all effects", pos = (0, 270), size = buttonSize)


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

        if filepath != "":
            self.wavInterface.set_orig_wavfile(filepath)

        root.destroy()


    def savefile(self, event):
        """Save a file"""
        root = tk.Tk()
        root.withdraw()

        dialogTitle = "Select a file"
        ftypes = [("WAV", ".wav")]

        filepath = filedialog.asksaveasfilename(initialdir = "./", title = dialogTitle, filetypes = ftypes, defaultextension = ".wav")

        if filepath != "":
            self.wavInterface.save_wavfile(filepath)

        root.destroy()
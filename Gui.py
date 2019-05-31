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
        
        ### Status boxes
        horiBoxSize = (600, 50)
        vertBoxSize = (120, 320)
        vertBoxHalfSize = (120, 160)
        buttonSize = (100, 50)
        textSize = (50, 20)

        infoBox = wx.StaticBox(mainPanel, wx.ID_ANY, "Track info", pos = (10, 0), size = horiBoxSize )
        playBox = wx.StaticBox(mainPanel, wx.ID_ANY, "Play", pos = (10, 50), size = vertBoxHalfSize )
        applyBox = wx.StaticBox(mainPanel, wx.ID_ANY, "Apply effects", pos = (10, 210), size = vertBoxHalfSize )
        echoBox = wx.StaticBox(mainPanel, wx.ID_ANY, "Echo", pos = (130, 50), size = vertBoxSize )
        distBox = wx.StaticBox(mainPanel, wx.ID_ANY, "Distortion", pos = (250, 50), size = vertBoxSize )
        temp1Box = wx.StaticBox(mainPanel, wx.ID_ANY, "Effect no. 3", pos = (370, 50), size = vertBoxSize )
        temp2Box = wx.StaticBox(mainPanel, wx.ID_ANY, "Effect no. 4", pos = (490, 50), size = vertBoxSize )

        # Info box
        self.trackNameText = wx.StaticText(mainPanel, wx.ID_ANY, "Track name: ", pos = (20, 20))
        self.trackLengthText = wx.StaticText(mainPanel, wx.ID_ANY, "Track length: ", pos = (420, 20))

        # Play box
        playOrigButton = wx.Button(mainPanel, wx.ID_ANY, "Play original", pos = (20, 80), size = buttonSize)
        self.Bind(wx.EVT_BUTTON, self.play_orig_wavfile, playOrigButton)

        playModiButton = wx.Button(mainPanel, wx.ID_ANY, "Play modified", pos = (20, 140), size = buttonSize)
        self.Bind(wx.EVT_BUTTON, self.play_modi_wavfile, playModiButton)

        # Apply effects box
        applyButton = wx.Button(mainPanel, wx.ID_ANY, "Apply all effects", pos = (20, 270), size = buttonSize)

        # Echo box
        echoCheck = wx.CheckBox(mainPanel, wx.ID_ANY, "Apply", pos = (140, 80))

        wx.StaticText(mainPanel, wx.ID_ANY, "Delay [s]", pos = (140, 120))
        echoDelayInput = wx.TextCtrl(mainPanel, wx.ID_ANY, pos = (140, 140), size = textSize)

        wx.StaticText(mainPanel, wx.ID_ANY, "Decay factor (0 - 1)", pos = (140, 180))
        echoDecayInput = wx.TextCtrl(mainPanel, wx.ID_ANY, pos = (140, 200), size = textSize)
        
        # Distortion box
        distCheck = wx.CheckBox(mainPanel, wx.ID_ANY, "Apply", pos = (260, 80))

        wx.StaticText(mainPanel, wx.ID_ANY, "Input gain (>1)", pos = (260, 120))
        echoDelayInput = wx.TextCtrl(mainPanel, wx.ID_ANY, pos = (260, 140), size = textSize)


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
            self.trackNameText.SetLabel("Track name: " + self.wavInterface.origWav.get_track_name()) 
            self.trackLengthText.SetLabel("Track length: " + self.wavInterface.origWav.get_track_length())
            
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


    def play_orig_wavfile(self, event):
        """Play original sound"""

        if self.wavInterface.origWav.fileName != "":
            self.wavInterface.origWav.play()


    def play_modi_wavfile(self, event):
        """Play modified sound"""

        if self.wavInterface.modiWav.fileName != "":
            self.wavInterface.modiWav.play()

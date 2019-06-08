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
        self.mainPanel = wx.Panel(self)
        self.Bind(wx.EVT_CLOSE, self.closewindow)

        ### Menu bar
        self.menuBar = wx.MenuBar()

        # 'File' menu
        self.fileMenu = wx.Menu()

        # File/Open
        self.fileOpen = self.fileMenu.Append(wx.ID_ANY, "Open")
        self.Bind(wx.EVT_MENU, self.openfile, self.fileOpen)

        # File/Save
        self.fileSave = self.fileMenu.Append(wx.ID_ANY, "Save as")
        self.Bind(wx.EVT_MENU, self.savefile, self.fileSave)

        # File/Exit
        self.fileExit = self.fileMenu.Append(wx.ID_EXIT, "Exit")
        self.Bind(wx.EVT_MENU, self.closewindow, self.fileExit)

        self.menuBar.Append(self.fileMenu, 'File')
        self.SetMenuBar(self.menuBar)
        
        ### Status boxes
        horiBoxSize = (600, 50)
        vertBoxSize = (120, 320)
        vertBoxHalfSize = (120, 160)
        buttonSize = (100, 40)
        textSize = (50, 20)

        wx.StaticBox(self.mainPanel, wx.ID_ANY, "Track info", pos = (10, 0), size = horiBoxSize )
        wx.StaticBox(self.mainPanel, wx.ID_ANY, "Play", pos = (10, 50), size = vertBoxHalfSize )
        wx.StaticBox(self.mainPanel, wx.ID_ANY, "Apply effects", pos = (10, 210), size = vertBoxHalfSize )
        wx.StaticBox(self.mainPanel, wx.ID_ANY, "Echo", pos = (130, 50), size = vertBoxSize )
        wx.StaticBox(self.mainPanel, wx.ID_ANY, "Distortion", pos = (250, 50), size = vertBoxSize )
        wx.StaticBox(self.mainPanel, wx.ID_ANY, "Tremolo", pos = (370, 50), size = vertBoxSize )
        wx.StaticBox(self.mainPanel, wx.ID_ANY, "Flanging", pos = (490, 50), size = vertBoxSize )

        # Info box
        self.trackNameText = wx.StaticText(self.mainPanel, wx.ID_ANY, "Track name: ", pos = (20, 20))
        self.trackLengthText = wx.StaticText(self.mainPanel, wx.ID_ANY, "Track length: ", pos = (420, 20))

        # Play box
        self.playOrigButton = wx.Button(self.mainPanel, wx.ID_ANY, "Play original", pos = (20, 80), size = buttonSize)
        self.Bind(wx.EVT_BUTTON, self.play_orig_wavfile, self.playOrigButton)

        self.playModiButton = wx.Button(self.mainPanel, wx.ID_ANY, "Play modified", pos = (20, 120), size = buttonSize)
        self.Bind(wx.EVT_BUTTON, self.play_modi_wavfile, self.playModiButton)

        self.stopButton = wx.Button(self.mainPanel, wx.ID_ANY, "Stop all", pos = (20, 160), size = buttonSize)
        self.Bind(wx.EVT_BUTTON, self.stop_all, self.stopButton)

        # Apply effects box
        self.applyEffectsButton = wx.Button(self.mainPanel, wx.ID_ANY, "Apply all effects", pos = (20, 250), size = buttonSize)
        self.Bind(wx.EVT_BUTTON, self.apply_effects, self.applyEffectsButton)

        self.resetEffectsButton = wx.Button(self.mainPanel, wx.ID_ANY, "Reset all effects", pos = (20, 290), size = buttonSize)
        self.Bind(wx.EVT_BUTTON, self.reset_effects, self.resetEffectsButton)

        # Echo box
        self.echoCheck = wx.CheckBox(self.mainPanel, wx.ID_ANY, "Apply", pos = (140, 80))

        wx.StaticText(self.mainPanel, wx.ID_ANY, "Delay [s]", pos = (140, 120))
        self.echoDelayInput = wx.TextCtrl(self.mainPanel, wx.ID_ANY, pos = (140, 140), size = textSize)

        wx.StaticText(self.mainPanel, wx.ID_ANY, "Decay factor (0 - 1)", pos = (140, 180))
        self.echoDecayInput = wx.TextCtrl(self.mainPanel, wx.ID_ANY, pos = (140, 200), size = textSize)

        # Distortion box
        self.distCheck = wx.CheckBox(self.mainPanel, wx.ID_ANY, "Apply", pos = (260, 80))

        wx.StaticText(self.mainPanel, wx.ID_ANY, "Input gain (>1)", pos = (260, 120))
        self.distGainInput = wx.TextCtrl(self.mainPanel, wx.ID_ANY, pos = (260, 140), size = textSize)

        # Tremolo box
        self.tremCheck = wx.CheckBox(self.mainPanel, wx.ID_ANY, "Apply", pos = (380, 80))

        wx.StaticText(self.mainPanel, wx.ID_ANY, "Depth (0 - 1)", pos  = (380, 120))
        self.tremDepthInput = wx.TextCtrl(self.mainPanel, wx.ID_ANY, pos = (380, 140), size = textSize)

        wx.StaticText(self.mainPanel, wx.ID_ANY, "fLFO [Hz] (2 - 10)", pos  = (380, 180))
        self.tremFLFOInput = wx.TextCtrl(self.mainPanel, wx.ID_ANY, pos = (380, 200), size = textSize)

        # Flanging box
        self.flangCheck = wx.CheckBox(self.mainPanel, wx.ID_ANY, "Apply", pos = (500, 80))

        wx.StaticText(self.mainPanel, wx.ID_ANY, "Delay [ms] (0.025 - 2)", pos  = (500, 120))
        self.flangDelayInput = wx.TextCtrl(self.mainPanel, wx.ID_ANY, pos = (500, 140), size = textSize)
        
        wx.StaticText(self.mainPanel, wx.ID_ANY, "Range (10 - 200)", pos  = (500, 180))
        self.flangRangeInput = wx.TextCtrl(self.mainPanel, wx.ID_ANY, pos = (500, 200), size = textSize)

        wx.StaticText(self.mainPanel, wx.ID_ANY, "fSweep [Hz] (0.25 - 2)", pos  = (500, 240))
        self.flangSweepInput = wx.TextCtrl(self.mainPanel, wx.ID_ANY, pos = (500, 260), size = textSize)


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
  
    
    def stop_all(self, event):
        """Stops all sound"""
        self.wavInterface.origWav.stop()


    def apply_echo(self):
        """Apply echo"""
        delay = int(self.echoDelayInput.GetValue())
        decayFactor = float(self.echoDelayInput.GetValue())
        self.wavInterface.apply_echo(delay, decayFactor)


    def apply_distortion(self):
        """Apply distortion"""
        inputGain = int(self.distGainInput.GetValue())
        self.wavInterface.apply_distortion(inputGain)


    def apply_tremolo(self):
        """Apply tremolo"""
        depth = float(self.tremDepthInput.GetValue())
        fLFO = float(self.tremFLFOInput.GetValue())
        self.wavInterface.apply_tremolo(depth, fLFO)


    def apply_flanging(self):
        """Apply flanging"""
        delay = float(self.flangDelayInput.GetValue())
        oscRange = int(self.flangRangeInput.GetValue())
        fSweep = float(self.flangSweepInput.GetValue())
        self.wavInterface.apply_flanging(delay, oscRange, fSweep)


    def apply_effects(self, event):
        """Apply all effects"""
  
        if self.distCheck.GetValue():
            self.apply_distortion()

        if self.tremCheck.GetValue():
            self.apply_tremolo()

        if self.flangCheck.GetValue():
            self.apply_flanging()

        if self.echoCheck.GetValue():
            self.apply_echo()


    def reset_effects(self, event):
        """Reset all effects"""
        self.wavInterface.reset_effects()
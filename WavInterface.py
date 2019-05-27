import numpy as np
import wavio
from WavUtils import *
import wx


class WavInterface:
    """Stores original and modified wav file
    """
    
    def __init__(self):
        self.origWav = WavFile()
        self.modiWav = WavFile()
        pass

    def set_orig_wavfile(self, file):
        """Initialize WavFile(file)"""

        if file != "":
            self.origWav = WavFile(file)
            self.modiWav = self.origWav

    def save_wavfile(self, file):
        """Saves a modified .WAV file"""
        
        if file != "":
            self.modiWav.write_to_file(file)
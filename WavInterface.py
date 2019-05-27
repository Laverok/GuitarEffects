import numpy as np
import wavio
from WavUtils import *
import wx


class WavInterface:

    def __init__(self):
        pass

    def set_orig_wavfile(self, file):
        """Initialize WavFile(file)"""

        if file != "":
            self.origWav = WavFile(file)

    def save_wavfile(self, file):
        """Saves a modivied .WAV file"""
        
        if file != "":
            self.modiWav.write_to_file(file)
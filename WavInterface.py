import numpy as np
import wavio
import copy
from WavUtils import *
import wx


class WavInterface:
    """Stores original and modified wav file
    """
    
    def __init__(self):
        self.origWav = WavFile()
        self.modiWav = WavFile()
        self.fileName = self.origWav.get_track_name()
        pass


    def set_orig_wavfile(self, file):
        """Initialize WavFile(file)"""

        if file != "":
            self.origWav = WavFile(file)
            self.modiWav = copy.deepcopy(self.origWav)


    def save_wavfile(self, file):
        """Saves a modified .WAV file"""
        
        if file != "":
            self.modiWav.write_to_file(file)


    def apply_echo(self, delay, decayFactor):
        """Apply echo to original wav file"""
        self.modiWav.echo_effect(delay, decayFactor)


    def apply_distortion(self, inputGain):
        """Apply distortion to original wav file"""
        self.modiWav.distortion_effect(inputGain)


    def apply_tremolo(self, depth, fLFO):
        """Appply tremolo to original wav file"""
        self.modiWav.tremolo_effect(depth, fLFO)

    
    def apply_flanging(self, delay, oscRange, fSweep):
        """Apply flanging to original wav file"""
        self.modiWav.flanging_effect(delay, oscRange, fSweep)
import wave
import pyaudio
import struct
import math
import numpy as np
import wavio
import simpleaudio as sa

class WavFile:

    def __init__(self, file):
        """Read the audio file and save all the important data"""
        self.wav = wavio.read(file)

        # framerate
        self.fs = self.wav.rate

        # track data
        self.data = self.wav.data

        # dimensions of the data which is (nSamples, nChannels)
        dim = np.shape(self.data)

        # number of samples in a file
        self.nSamples = dim[0]

        # number of channels, 1 - mono, 2 - stereo
        self.nChannels = dim[1]

        # length of a file in seconds
        self.length = self.nSamples / self.fs

        # number of bytes per sample
        self.bytes = self.wav.sampwidth


    def play(self):
        """Play the file"""
        play = sa.play_buffer(self.data, self.nChannels, self.bytes, self.fs)
        play.wait_done()


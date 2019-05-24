import wave
import pyaudio
import struct
import math
import numpy as np
import simpleaudio as sa

class WavFile:

    chunk = 1024

    def __init__(self, file):
        """Initialize audio stream and save all information"""
        self.wav = wave.open(file, 'r')
        self.fileName = file

        # framerate
        self.fs = self.wav.getframerate()

        # number of frames in a file
        self.frames = self.wav.getnframes() 

        # length of a file in seconds
        self.length = self.frames / self.fs 

        # number of bytes per sample
        self.bytes = self.wav.getsampwidth() 

        # number of channels, 1 - mono, 2 - stereo
        self.channels = self.wav.getnchannels() 

        # save data as an array
        self.samples = []

      
        for i in range(0, self.frames):
            wavData = self.wav.readframes(1)
            data = struct.unpack("%ih"%self.channels, wavData)
            self.samples.append(int(data[0]))

        self.samples = np.array(self.samples)
        self.wav.close()


    def play(self):
        """Play the file"""
        play = sa.play_buffer(self.samples, self.channels, self.bytes, self.fs)
        play.wait_done()


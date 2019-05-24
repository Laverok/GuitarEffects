import wave
import pyaudio
import struct
import math
from numpy import array

class WavFile:

    chunk = 1024

    def __init__(self, file):
        """Initialize audio stream"""
        self.wav = wave.open(file, 'r')
        self.fs = self.wav.getframerate() # framerate
        self.frames = self.wav.getnframes() # number of frames in a file
        self.length = self.frames / self.fs # length of a file in seconds
        self.bytes = self.wav.getsampwidth() # number of bytes per sample
        self.channels = self.wav.getnchannels() # number of channels, 1 - mono, 2 - stereo
        

    def play(self):
        """Play the file"""
        p = pyaudio.PyAudio()
        stream = p.open(
            format = p.get_format_from_width(self.bytes),
            channels = self.channels,
            rate = self.fs,
            output = True
        )

        wavData = self.wav.readframes(self.chunk)
        while len(wavData) > 0:
            stream.write(wavData)
            wavData = self.wav.readframes(self.chunk)
        
        stream.stop_stream()
        stream.close()
        p.terminate()

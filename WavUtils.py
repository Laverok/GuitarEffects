import wave
import pyaudio
import struct
import math

class WavFile:

    chunk = 1024

    def __init__(self, file):
        """Initialize audio stream"""
        self.wav = wave.open(file, 'r')
        self.fileName = file
        self.fs = self.wav.getframerate() # framerate
        self.frames = self.wav.getnframes() # number of frames in a file
        self.length = self.frames / self.fs # length of a file in seconds
        self.bytes = self.wav.getsampwidth() # number of bytes per sample
        self.channels = self.wav.getnchannels() # number of channels, 1 - mono, 2 - stereo
        self.wav.close()

    def play(self):
        """Play the file"""
        wav = wave.open(self.fileName, 'r')
        p = pyaudio.PyAudio()
        stream = p.open(
            format = p.get_format_from_width(self.bytes),
            channels = self.channels,
            rate = self.fs,
            output = True
        )

        wavData = wav.readframes(self.chunk)
        while len(wavData) > 0:
            stream.write(wavData)
            wavData = wav.readframes(self.chunk)
        
        wav.close()
        stream.stop_stream()
        stream.close()
        p.terminate()


    def get_samples(self):
        """Return an array of samples"""
        wav = wave.open(self.fileName, 'r')
        samples = []
        length = wav.getnframes()

        for i in range(0, length):
            wavData = wav.readframes(1)
            data = struct.unpack("%ih"%2, wavData)
            samples.append(int(data[0]))

        wav.close()
        return samples
import wave
import pyaudio
import struct
import math

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
            data = struct.unpack("%ih"%2, wavData)
            self.samples.append(int(data[0]))

        self.wav.close()


    def play(self):
        """Play the file"""
        wav = wave.open(self.fileName, 'r')
        p = pyaudio.PyAudio()

        # opens the audio stream
        stream = p.open(
            format = p.get_format_from_width(self.bytes),
            channels = self.channels,
            rate = self.fs,
            output = True
        )

        # reads the audio stream until the end of it
        wavData = wav.readframes(self.chunk)
        while len(wavData) > 0:
            stream.write(wavData)
            wavData = wav.readframes(self.chunk)
        
        # clean-up
        wav.close()
        stream.stop_stream()
        stream.close()
        p.terminate()

import wave
import pyaudio

class WavFile:

    chunk = 1024

    def __init__(self, file):
        """Initialize audio stream"""
        self.wav = wave.open(file, 'rb')
        self.fs = self.wav.getframerate() # framerate
        self.frames = self.wav.getnframes() # number of frames in a file
        self.length = self.frames / self.fs # length of a file in seconds
        self.bytes = self.wav.getsampwidth() # number of bytes per sample
        self.channels = self.wav.getnchannels() # number of channels, 1 - mono, 2 - stereo
        
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format = self.p.get_format_from_width(self.bytes),
            channels = self.channels,
            rate = self.fs,
            output = True
        )


    def play(self):
        """Play the file"""
        wav_data = self.wav.readframes(self.chunk)

        while len(wav_data) > 0:
            self.stream.write(wav_data)
            wav_data = self.wav.readframes(self.chunk)


    def close(self):
        """Close the file"""
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
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
        self.data = np.array(self.wav.data)

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
        """Play the sound"""
        play = sa.play_buffer(self.data, self.nChannels, self.bytes, self.fs)
        play.wait_done()


    def write_to_file(self, file):
        """Save file in a .wav format"""
        wavio.write(file, self.data, self.fs, scale = 'none', sampwidth = self.bytes)

   
    def echo_effect(self, delay, decayFactor ):
        """Add echo effect

           delay: in seconds
           decayFactor: [0,1]  
        """
        # convert delay in seconds to delay in number of samples
        delaySamples = delay * self.fs
    
        for i in range(delaySamples, self.nSamples):
            
            current = self.data[i]
            edited = self.data[i - delaySamples] * decayFactor
            
            current += edited.astype(int)
        
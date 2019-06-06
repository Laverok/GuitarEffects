import numpy as np
import wavio
import simpleaudio as sa


class WavFile:
    """Class representing a .WAV file

       file: path to the .wav file
    """
    def __init__(self, file = ""):
        """Read the audio file and save all the important data"""

        self.fileName = file
        
        if file != "":
            self.wav = wavio.read(file)

            # framerate
            self.fs = self.wav.rate

            # track data
            self.data = np.array(self.wav.data)

            # dimensions of the data which is (nSamples, nChannels)
            # nSamples: number of samples in a file
            # nChannels: number of channels, 1 - mono, 2 - stereo
            (self.nSamples, self.nChannels) = np.shape(self.data)

            # length of a file in seconds
            self.length = self.nSamples / self.fs

            # number of bytes per sample
            self.bytes = self.wav.sampwidth


    def get_track_name(self):
        """Return a track name 'name.wav' """
        lastSlashIndex = self.fileName.rfind('/')

        return self.fileName[lastSlashIndex + 1:]


    def get_track_length(self):
        """Return a string in a format 'hh/mm/ss' """
        h = int(self.length / 3600)
        m = int((self.length - h * 3600) / 60)
        s = int(self.length - h * 3600 - m * 60)

        hStr, mStr, sStr = "", "", ""

        if h == 0:
            hStr = "00"
        elif h > 9:
            hStr = str(h)
        else:
            hStr = "0"+str(h)

        if m == 0:
            mStr = "00"
        elif m > 9:
            mStr = str(m)
        else:
            mStr = "0"+str(m)

        if s == 0:
            sStr = "00"
        elif s > 9:
            sStr = str(s)
        else:
            sStr = "0"+str(s)

        time = hStr + ":" + mStr + ":" + sStr
        return time


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
           decayFactor: 0-1 
        """
        # convert delay in seconds to delay in number of samples
        delaySamples = delay * self.fs
    
        for i in range(delaySamples, self.nSamples):
            
            current = self.data[i]
            edited = self.data[i - delaySamples] * decayFactor
            
            current += edited.astype(dtype = np.int16)
        

    def distortion_effect(self, inputGain):
        """Add distortion effect (exponential function)

           inputGain: the higher the more distortion
        """ 
        # scale factor so the algorithm works properly
        # 32768 for 16-bit .wav
        sFactor = 2**((self.bytes * 8) - 1)
        scaledData = (self.data).astype(float) / sFactor

        tempData = np.empty(np.shape(scaledData))
        for i in range(self.nSamples):
             
            sign = np.sign(scaledData[i])
            tempData[i] = sign * (1 - np.exp(-np.abs(scaledData[i] * inputGain)))

        tempData *= sFactor
        self.data = tempData.astype(dtype = np.int16)


    def tremolo_effect(self, depth, fLFO):
        """Add tremolo effect
        
        depth:     0-1
        fLFO(Hz):  2-10
        """

        fNorm = 2 * np.pi * fLFO / self.fs;

        tempData = np.empty(np.shape(self.data), dtype = np.int16)

        for i in range(0, self.nSamples):
            tempData[i] = self.data[i] * round((1 + depth * np.cos(fNorm * i)))

        self.data = tempData


    def flanging_effect(self, delay, oscRange, fSweep):
        """Add flanging effect
        
        delay(ms): 0.025-2
        oscRange:     10-200
        fSweep(Hz):   0.25-2
        """
        
        delaySamples = round(delay / 1000 * self.fs);
        
        fNorm = 2 * np.pi * fSweep/self.fs;

        tempData = np.empty(np.shape(self.data), dtype = np.int16)

        for i in range(0, self.nSamples-delaySamples-oscRange):
            
            tempData[i] = self.data[i] + self.data[i+delaySamples+int(round(oscRange*np.sin(fNorm * i)))]

        self.data = tempData

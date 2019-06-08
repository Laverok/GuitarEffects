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

            # number of bytes per sample
            self.bytes = self.wav.sampwidth

            # track data
            self.data = np.array(self.wav.data)

            #track data as float
            self.floatData = int_to_float(self.data, self.bytes)

            # dimensions of the data which is (nSamples, nChannels)
            # nSamples: number of samples in a file
            # nChannels: number of channels, 1 - mono, 2 - stereo
            (self.nSamples, self.nChannels) = np.shape(self.data)

            # length of a file in seconds
            self.length = self.nSamples / self.fs

            
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


    def stop(self):
        """Stop all sounds"""
        sa.stop_all()


    def write_to_file(self, file):
        """Save file in a .wav format"""
        wavio.write(file, self.data, self.fs, scale = 'none', sampwidth = self.bytes)

   
    def echo_effect(self, delay, decayFactor ):
        """Add echo effect

           delay[s]: >0.0
           decayFactor: 0-1 
        """
        # convert delay in seconds to delay in number of samples
        delaySamples = int(delay * self.fs)

        tempData = np.empty(np.shape(self.floatData), dtype = np.float)

        for i in range(0, self.nSamples):
            
            if i >= delaySamples:
                tempData[i] = self.floatData[i] + decayFactor * self.floatData[i - delaySamples]
            else:
                tempData[i] = self.floatData[i]

        self.floatData = tempData
        self.data = float_to_int16(tempData)


    def distortion_effect(self, inputGain):
        """Add distortion effect (implemented with an exponential function)

           inputGain: 2-20
        """ 

        tempData = np.empty(np.shape(self.floatData), dtype = np.float)

        for i in range(self.nSamples):
             
            sign = np.sign(self.floatData[i])
            tempData[i] = sign * (1 - np.exp(-np.abs(self.floatData[i] * inputGain)))

        self.floatData = tempData
        self.data = float_to_int16(tempData)


    def tremolo_effect(self, depth, fLFO):
        """Add tremolo effect
        
        depth:     0-1
        fLFO(Hz):  2-10
        """

        fNorm = 2 * np.pi * fLFO / self.fs;

        tempData = np.empty(np.shape(self.floatData), dtype = np.float)

        for i in range(0, self.nSamples):
            tempData[i] = self.floatData[i] * (1 + depth * np.cos(fNorm * i))

        self.floatData = tempData
        self.data = float_to_int16(tempData)


    def flanging_effect(self, delay, oscRange, fSweep):
        """Add flanging effect
        
        delay(ms):    0.025-2
        oscRange:     10-200
        fSweep(Hz):   0.25-2
        """
        
        delaySamples = round(delay / 1000 * self.fs);
        
        fNorm = 2 * np.pi * fSweep/self.fs;

        tempData = np.empty(np.shape(self.floatData), dtype = np.float)

        for i in range(0, self.nSamples-delaySamples-oscRange):
            
            tempData[i] = self.floatData[i] + self.floatData[i+delaySamples+int(round(oscRange*np.sin(fNorm * i)))]

        self.floatData = tempData
        self.data = float_to_int16(tempData)



def int_to_float(intArray, nBytes):
    """Convert an int array to a float array"""
    
    floatArray = np.empty(np.shape(intArray), dtype = np.float)
    floatArray = intArray / 2 ** (8 * nBytes - 1)

    return floatArray


def float_to_int16(floatArray):
    """Convert a float array to an int16 array"""

    intArray = np.empty(np.shape(floatArray), dtype = np.int16)

    arrayMax = np.amax(floatArray)
    arrayMin = np.amin(floatArray)
    scaleFactor = arrayMax if arrayMax >= np.abs(arrayMin) else np.abs(arrayMin)

    intArray = (floatArray / scaleFactor * 2**15).astype(np.int16)

    return intArray
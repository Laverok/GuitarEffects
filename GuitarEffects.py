import wave
import pyaudio
import struct
import math
from numpy.fft import *
import matplotlib.pyplot as plt
import WavUtils as util

wavTrack = util.WavFile("./sample/stereo/Roundabout.wav")

wavTrack.play()
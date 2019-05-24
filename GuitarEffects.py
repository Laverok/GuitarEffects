import wave
import pyaudio
import struct
import math
import numpy as np
import WavUtils as util

wavTrack = util.WavFile("./sample/stereo/SanSalvadorr.wav")

wavTrack.play()

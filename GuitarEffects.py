import wave
import pyaudio
import struct
import math
import WavUtils as util

wavTrack = util.WavFile("./sample/stereo/Roundabout.wav")

wavTrack.play()
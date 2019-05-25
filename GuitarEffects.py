import math
import numpy as np
import wavio
import simpleaudio as sa
import WavUtils as util

wavTrack = util.WavFile("./sample/stereo/SanSalvadorr.wav")

wavTrack.write_to_file("./output/out2.wav")
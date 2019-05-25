import numpy as np
import wavio
import simpleaudio as sa
import WavUtils as util

wavTrack = util.WavFile("./sample/stereo/Roundabout.wav")

wavTrack.echo_effect(2, 0.4)
wavTrack.play()
wavTrack.write_to_file("./output/out2.wav")
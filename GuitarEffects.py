import numpy as np
import wavio
import WavUtils as util

wavTrack = util.WavFile("./sample/stereo/Do rana.wav")

#wavTrack.echo_effect(2, 0.4)
wavTrack.distortion_effect(6)
wavTrack.play()
wavTrack.write_to_file("./output/out.wav" )
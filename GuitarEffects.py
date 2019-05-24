import wave
import pyaudio
import WavUtils as util

console_input = "./sample/stereo/SanSalvadorr.wav"
wavData = util.WavFile(console_input)

wavData.play()
wavData.close()
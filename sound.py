import sounddevice as sd
import numpy as np
import wave
import warnings

def oto():
    warnings.simplefilter('ignore')
    file_n="./input.wav"
    length=5
    sampling=16000
    sd.default.samplerate = sampling
    sd.default.channels = 1
    sd.default.dtype = 'float64'

    data=sd.rec(int(length*sampling),sampling,channels=1)

    sd.wait()
    data= data / data.max() * np.iinfo(np.int16).max  #exchange nomalize

    #float->int
    data=data.astype(np.int16)

    #save file

    with wave.open(file_n, mode="wb")as wb:
        wb.setnchannels(1)
        wb.setsampwidth(2)
        wb.setframerate(sampling)
        wb.writeframes(data.tobytes())#exchange byte

    
    
    
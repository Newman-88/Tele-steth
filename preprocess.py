import pyaudio
import wave
import sounddevice as sd
import struct
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import butter, lfilter

##### The program is written to test the "effectiveness of the custum_filter" function.
##### The testing can be done either by already recorded data (rawdata_1.wav, etc) or by live recording using DIY diaphragm.

#### Ask the mode to test(recorded data or live recording):
def ask_mode():
    try:
        mode = int(input("Please enter the mode of testing\n'recorded data' = 1 or 'live recording' =  2\nEnter 1 or 2: "))
        if mode ==1 or mode ==2:
            return (mode)
        else:
            mode = ask_mode()
            return (mode)
    except:
        mode = ask_mode()
        return (mode)
    
#################..............define the function custum_filter..........######
##--------------------CONCENTRATE ON THIS PART OF THE CODE----------------------
##
def custum_filter(raw_data, fs):
    '''The main function which does filtering of the raw data.
    Inputs are raw data chunk and sampling frequency and outpus processed data'''

    lowcut = 10
    highcut = 30
    order = 1
    processed_data = butter_bandpass_filter(raw_data, lowcut, highcut, fs, order)

    
    ## normalizing the data
    processed_data = processed_data/max(processed_data)
    return (processed_data)

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y
##
##---------------------------------------------------------------------------------
############...........define function for recorded data testing:
def recorded_data_test():
    filename = input("Please enter the test file name with extension(.wav): ")
    fs, raw_data = wavfile.read(filename)

    processed_data = custum_filter(raw_data, fs)

    return (raw_data,processed_data,fs)

############..........define function for live record testing:
def live_record_test():
    pass


    
###########........main function of the program: 
mode = ask_mode()
print(mode)
if mode ==1:
    raw_data,processed_data,fs = recorded_data_test()
else:
    raw_data,processed_data,fs = live_record_test()


print(type(raw_data[0]))
print(type(processed_data[0]))
####....Displaying both raw_data and processed_data:
plt.subplot(2,1,1)
plt.plot(raw_data)
plt.title("Raw_data")

plt.subplot(2,1,2)
plt.plot(processed_data)
plt.title("Processed_data")

plt.show()

####....play both sounds one by one:
print("Playing raw_sound")
sd.play(raw_data,fs)
sd.wait()

print("Playing processed_sound")
sd.play(processed_data,fs)
sd.wait()

print("Finished Testing")

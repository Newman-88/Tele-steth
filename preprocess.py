import pyaudio
import wave
import sounddevice as sd
import struct
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import butter, sosfilt, sosfreqz

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

    lowcut = 20
    highcut = 150
    order = 6

    ## normalizing the data
    data = raw_data/max(raw_data)
    processed_data = butter_bandpass_filter(data, lowcut, highcut, fs, order)

    
    
    return (processed_data)



def butter_bandpass(lowcut, highcut, fs, order):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        sos = butter(order, [low, high], analog=False, btype='band', output='sos')
        return sos

def butter_bandpass_filter(data, lowcut, highcut, fs, order):
        sos = butter_bandpass(lowcut, highcut, fs, order=order)
        y = sosfilt(sos, data)
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
    CHUNK = 1024
    FORMAT = pyaudio.paFloat32
    CHANNELS = 1
    fs = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    stream1 = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=fs,
                input=True,
                input_device_index = 1,
                frames_per_buffer=CHUNK)

    stream2 = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=fs,
                output=True,
                frames_per_buffer=CHUNK)

    print("* recording")

    raw_data = []
    for i in range(0, int(fs / CHUNK * RECORD_SECONDS)):
        data = stream1.read(CHUNK)
            
    ########################
        stream2.write(data)
        dd = np.fromstring(data, 'Float32')
        raw_data = np.append(raw_data,dd)
    
    print("* done recording")

    stream1.stop_stream()
    stream1.close()
    stream2.stop_stream()
    stream2.close()
    p.terminate()

    processed_data = custum_filter(raw_data, fs)
    return (raw_data,processed_data,fs)
    
###########........main function of the program:
def main(): 
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

if __name__ == "__main__":
    main()

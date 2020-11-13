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
    highcut = 180
    order = 6

    ## normalizing the data
    raw_data = raw_data/max(abs(raw_data))
    processed_data = butter_bandpass_filter(raw_data, lowcut, highcut, fs, order)
    #processed_data = processed_data/max(abs(processed_data))
    processed_data = processed_data*30000
    processed_data = processed_data.astype('int16')
    
    
    
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

    return (raw_data,processed_data,fs, processed_data)

############..........define function for live record testing:
def live_record_test():
    CHUNK = 1028
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    fs = 2056
    RECORD_SECONDS = 10
   

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
    filt_data_test = []
    for i in range(0, int(fs / CHUNK * RECORD_SECONDS)):
        data = stream1.read(CHUNK)
            
    ########################
        dd = np.frombuffer(data, dtype= np.int16)
        raw_data = np.append(raw_data,dd)

        filt_data = custum_filter(dd, fs)
        filt_data.tobytes()

        stream2.write(filt_data)
        filt_data_test = np.append(filt_data_test, filt_data)

        
        
    print("* done recording")

    stream1.stop_stream()
    stream1.close()
    stream2.stop_stream()
    stream2.close()
    p.terminate()

    processed_data = custum_filter(raw_data, fs)
    
    return (raw_data,processed_data,fs, filt_data_test)
    
###########........main function of the program:
def main(): 
    mode = ask_mode()
    print(mode)
    if mode ==1:
        raw_data,processed_data,fs = recorded_data_test()
    else:
        raw_data,processed_data,fs,filt_data_test = live_record_test()


    print(type(raw_data[0]))
    print(type(processed_data[0]))
    print(type(filt_data_test[0]))
    ####....Displaying both raw_data and processed_data:
    plt.subplot(3,1,1)
    plt.plot(raw_data)
    plt.title("Raw_data")

    plt.subplot(3,1,2)
    plt.plot(filt_data_test)
    plt.title("Chunk_Processed_data")
    
    plt.subplot(3,1,3)
    plt.plot(processed_data)
    plt.title("Processed_data")
    plt.show()

    ####....play both sounds one by one:
    print("Playing raw_sound")
    sd.play(raw_data,fs)
    raw_data = raw_data/max(abs(raw_data))
    sd.wait()

    print("Playing chunk processed_sound")
    filt_data_test = filt_data_test/max(abs(filt_data_test))
    sd.play(filt_data_test,fs)
    sd.wait()


    print("Playing processed_sound")
    sd.play(processed_data,fs)
    sd.wait()

    print("Finished Testing")

    filt_data_test = filt_data_test.astype('float32')
    wavfile.write("rec_1.wav", fs, filt_data_test)
    

if __name__ == "__main__":
    main()

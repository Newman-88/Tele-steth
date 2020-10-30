import socket
import threading
import pyaudio
import numpy as np

####### Import custum_filter function from preprocess.py for data processing 
from preprocess import custum_filter

### Define class which would stream the data 
class Client:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        while 1:
            try:
                self.target_ip = input('Enter IP address of server --> ')
                self.target_port = int(input('Enter target port of server --> '))

                self.s.connect((self.target_ip, self.target_port))

                break
            except:
                print("Couldn't connect to server")

        chunk_size = 1024 # 512
        audio_format = pyaudio.paFloat32
        channels = 1
        rate = 2048

        # initialise microphone recording
        self.p = pyaudio.PyAudio()
        #self.playing_stream = self.p.open(format=audio_format, channels=channels, rate=rate, output=True, frames_per_buffer=chunk_size)
        self.recording_stream = self.p.open(format=audio_format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk_size)
        
        print("Connected to Server")

        # start threads
        #receive_thread = threading.Thread(target=self.receive_server_data).start()
        self.send_data_to_server(rate)

    def receive_server_data(self):
        while True:
            try:
                data = self.s.recv(1024)
                self.playing_stream.write(data)
            except:
                pass

    ### Sending the data to server 
    def send_data_to_server(self, rate):
        while True:
            try:
                data = self.recording_stream.read(1024)
                dd = np.fromstring(data, 'Float32')
    ##########...................Processing data before sending to the server:...........................###################################
                processed_data = custum_filter(dd, rate)
                processed_data.tobytes()
                self.s.sendall(processed_data)
            except:
                pass

client = Client()

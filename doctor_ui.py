from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import threading
import pyaudio
import numpy as np
import matplotlib.pyplot as plt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(726, 577)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 50, 700, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 180, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(350, 180, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(490, 180, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(120, 10, 75, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(120, 92, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.ipaddress = QtWidgets.QLineEdit(self.centralwidget)
        self.ipaddress.setGeometry(QtCore.QRect(200, 90, 171, 20))
        self.ipaddress.setObjectName("ipaddress")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(410, 92, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.port = QtWidgets.QLineEdit(self.centralwidget)
        self.port.setGeometry(QtCore.QRect(450, 90, 101, 20))
        self.port.setObjectName("port")
        self.connect_pat = QtWidgets.QPushButton(self.centralwidget)
        self.connect_pat.setGeometry(QtCore.QRect(250, 130, 180, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.connect_pat.setFont(font)
        self.connect_pat.setObjectName("connect_pat")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 10, 211, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 182, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(390, 182, 47, 13))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(530, 182, 47, 13))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(200, 210, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(370, 210, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.conn_status = QtWidgets.QLabel(self.centralwidget)
        self.conn_status.setGeometry(QtCore.QRect(290, 155, 141, 20))
        self.conn_status.setObjectName("conn_status")
        self.record = QtWidgets.QPushButton(self.centralwidget)
        self.record.setGeometry(QtCore.QRect(250, 260, 150, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.record.setFont(font)
        self.record.setObjectName("record")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.out_image = QtWidgets.QLabel(self.centralwidget)
        self.out_image.setGeometry(QtCore.QRect(50, 300, 620, 200))
        self.out_image.setText("")
        self.out_image.setScaledContents(True)
        self.out_image.setObjectName("out_image")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.connect_pat.clicked.connect(lambda: self.clicked())
        self.record.clicked.connect(lambda: self.clicked_rec())

        self.rcvd_data = []

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Telesthoscope-Doctor_UI"))
        self.label.setText(_translate("MainWindow", "Please enter the IP address and port to connect to your doctor"))
        self.label_3.setText(_translate("MainWindow", "Name:"))
        self.label_4.setText(_translate("MainWindow", "Age:"))
        self.label_5.setText(_translate("MainWindow", "Sex:"))
        self.label_6.setText(_translate("MainWindow", "Patient ID:"))
        self.label_7.setText(_translate("MainWindow", "IP Address:"))
        self.label_8.setText(_translate("MainWindow", "Port:"))
        self.connect_pat.setText(_translate("MainWindow", "Connect to Patient"))
        self.label_2.setText(_translate("MainWindow", "XX"))
        self.label_9.setText(_translate("MainWindow", "--"))
        self.label_10.setText(_translate("MainWindow", "--"))
        self.label_11.setText(_translate("MainWindow", "Auscultation Area:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Mitral"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Aortic"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Pulmonary"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Tricuspid"))
        self.conn_status.setText(_translate("MainWindow", "      (Not connected)"))
        self.record.setText(_translate("MainWindow", "Start Recording"))

    def clicked(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.chunk_size = 1024 # 512
        self.audio_format = pyaudio.paInt16
        self.channels = 1
        self.rate = 2048
        
        if self.connect_pat.text() == "Connect to Patient":
        
            try:
                self.ip = self.ipaddress.text()
                self.port_no = int(self.port.text())
                self.s.connect((self.ip, self.port_no))
                self.start()
                self.conn_status.setText("          (Connected)")
                self.connect_pat.setText("  Disconnect")
                
            except:
                self.conn_status.setText("      (Incorrect Details)")

        else:
            self.s.close()
            self.conn_status.setText("       (Not Connected)")
            self.connect_pat.setText("Connect to Patient")

    def start(self):

        # initialise microphone recording
        self.p = pyaudio.PyAudio()
        self.playing_stream = self.p.open(format=self.audio_format, channels=self.channels, rate=self.rate, output=True, frames_per_buffer=self.chunk_size)
        #self.recording_stream = self.p.open(format=audio_format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk_size)
        
        #print("Connected to Server")

        # start threads
        receive_thread = threading.Thread(target=self.receive_server_data).start()
        #self.send_data_to_server()

    def receive_server_data(self):
        while True:
            try:
                data = self.s.recv(2096)
                self.playing_stream.write(data)
                if self.record.text()== "Stop Recording":
                    numpy_data = np.frombuffer(data, dtype = np.int16)
                    self.rcvd_data = np.append(self.rcvd_data, numpy_data)
                #print(sys.getsizeof(data))
                    
            except:
                pass

    def clicked_rec(self):
        if self.record.text() == "Start Recording":
            self.record.setText("Stop Recording")
        else:
            self.record.setText("Start Recording")
            if len(self.rcvd_data)!=0:
                plt.plot(self.rcvd_data)
                plt.savefig("test.svg",format="svg",bbox_inches="tight")
                plt.close()
                self.rcvd_data = []
                try:
                    self.out_image.setPixmap(QtGui.QPixmap("test.svg"))
                except:
                    pass
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

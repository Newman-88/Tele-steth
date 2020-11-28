from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import threading
import pyaudio
import numpy as np
from preprocess import custum_filter


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(726, 577)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(200, 280, 331, 271))
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("card_area.bmp"))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 130, 541, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 250, 521, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 10, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 40, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 70, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(120, 100, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(190, 70, 71, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 10, 241, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(190, 40, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 100, 221, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(120, 170, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.ipaddress = QtWidgets.QLineEdit(self.centralwidget)
        self.ipaddress.setGeometry(QtCore.QRect(200, 170, 171, 20))
        self.ipaddress.setObjectName("ipaddress")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(420, 170, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.port = QtWidgets.QLineEdit(self.centralwidget)
        self.port.setGeometry(QtCore.QRect(460, 170, 101, 20))
        self.port.setObjectName("port")
        self.connect_doc = QtWidgets.QPushButton(self.centralwidget)
        self.connect_doc.setGeometry(QtCore.QRect(300, 200, 141, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.connect_doc.setFont(font)
        self.connect_doc.setObjectName("connect_doc")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(303, 223, 141, 20))
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.connect_doc.clicked.connect(lambda: self.clicked())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Telesthoscope-Patient_UI"))
        self.label.setText(_translate("MainWindow", "Please enter the IP address and port to connect to your doctor"))
        self.label_2.setText(_translate("MainWindow", "Please Keep the Telestethoscope diaphragm as depicted below"))
        self.label_3.setText(_translate("MainWindow", "Name: "))
        self.label_4.setText(_translate("MainWindow", "Age:"))
        self.label_5.setText(_translate("MainWindow", "Sex:"))
        self.label_6.setText(_translate("MainWindow", "Patient ID:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Male"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Female"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Others"))
        self.label_7.setText(_translate("MainWindow", "IP Address:"))
        self.label_8.setText(_translate("MainWindow", "Port:"))
        self.connect_doc.setText(_translate("MainWindow", "Connect to Doctor"))
        self.label_9.setText(_translate("MainWindow", "          (Not Connected)"))

    def clicked(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.chunk_size = 1024 # 512
        self.audio_format = pyaudio.paInt16
        self.channels = 1
        self.rate = 2048
        
        if self.connect_doc.text() == "Connect to Doctor":
        
            try:
                self.ip = self.ipaddress.text()
                self.port_no = int(self.port.text())
                self.s.connect((self.ip, self.port_no))
                self.label_9.setText("             (Connected)")
                self.connect_doc.setText("   Disconnect")
                self.start()
                
            except:
                self.label_9.setText("        (Incorrect Details)")

        else:
            self.s.close()
            self.label_9.setText("         (Not Connected)")

            self.connect_doc.setText("Connect to Doctor")

    def start(self):

        # initialise microphone recording
        self.p = pyaudio.PyAudio()
        #self.playing_stream = self.p.open(format=self.audio_format, channels=self.channels, rate=self.rate, output=True, frames_per_buffer=self.chunk_size)
        self.recording_stream = self.p.open(format=self.audio_format, channels=self.channels, rate=self.rate, input=True, frames_per_buffer=self.chunk_size)
        send_thread = threading.Thread(target=self.send_data_to_server)
        send_thread.start()
        #self.send_data_to_server()

    def send_data_to_server(self):
        while True:
            try:
                data = self.recording_stream.read(1024)
                if self.comboBox.currentIndex()==0:
                    dd = np.frombuffer(data, dtype= np.int16)
    ##########...................Processing data before sending to the server:...........................###################################
                    processed_data = custum_filter(dd, self.rate)
                    processed_data.tobytes()
                    self.s.sendall(processed_data)
                else:
                    self.s.sendall(data)
                #print(sys.getsizeof(processed_data))
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

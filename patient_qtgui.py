# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 12:34:00 2020

@author: Ausath
"""

from PyQt5 import QtWidgets

class Main_Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        return
    
    def setup_ui(self):
        self.setWindowTitle('Telestethoscope(Patient)')
        
        central_layout = QtWidgets.QHBoxLayout()
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)
        
        main_layout = QtWidgets.QVBoxLayout()
        central_layout.addLayout(main_layout, 9)
        details_layout = QtWidgets.QHBoxLayout()
        main_layout.addLayout(details_layout, 4)
        interaction_layout = QtWidgets.QHBoxLayout()
        main_layout.addLayout(interaction_layout, 6)
        button_layout = QtWidgets.QVBoxLayout()
        central_layout.addLayout(button_layout, 1)
        
        patient_box = QtWidgets.QGroupBox('Patient Summary')
        details_layout.addWidget(patient_box)
        patient_layout = QtWidgets.QFormLayout()
        patient_box.setLayout(patient_layout)
        self.patient_id = QtWidgets.QLineEdit()
        patient_layout.addRow('Patient ID', self.patient_id)
        self.patient_name = QtWidgets.QLineEdit()
        patient_layout.addRow('Name', self.patient_name)
        self.patient_age = QtWidgets.QLineEdit()
        patient_layout.addRow('Age', self.patient_age)
        self.patient_sex = QtWidgets.QComboBox()
        self.patient_sex.addItems(['Male', 'Female', 'Transgender'])
        patient_layout.addRow('Sex', self.patient_sex)
        
        connection_box = QtWidgets.QGroupBox('Connections')
        details_layout.addWidget(connection_box)
        connection_layout = QtWidgets.QFormLayout()
        connection_box.setLayout(connection_layout)
        self.server_ip = QtWidgets.QLineEdit()
        connection_layout.addRow('Server IP Address', self.server_ip)
        self.server_port = QtWidgets.QLineEdit()
        connection_layout.addRow('Server Port', self.server_port)
        self.doctors_list = QtWidgets.QComboBox()
        connection_layout.addRow('Doctor ID', self.doctors_list)
        self.get_doctor = QtWidgets.QPushButton('Ask Your Doctor')
        self.get_doctor.clicked.connect(self.doctor_connect)
        connection_layout.addRow(self.get_doctor)
        
        image_layout = QtWidgets.QGridLayout()
        interaction_layout.addLayout(image_layout, 7)
        positions = [(i,j) for i in range(2) for j in range(2)]
        for position in positions:
            label = QtWidgets.QLabel('Image ' + str(position))
            label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, 
                                QtWidgets.QSizePolicy.Expanding)
            image_layout.addWidget(label, *position)
        
        chat_box = QtWidgets.QGroupBox('Chat Box')
        interaction_layout.addWidget(chat_box, 3)
        chat_layout = QtWidgets.QVBoxLayout()
        chat_box.setLayout(chat_layout)
        self.chat_history = QtWidgets.QTextEdit()
        self.chat_history.setReadOnly(True)
        chat_layout.addWidget(self.chat_history)
        self.chat_line = QtWidgets.QLineEdit()
        self.chat_line.enterEvent.connect(self.update_chat)
        chat_layout.addWidget(self.chat_line)
        
        buttons = ('Connect', 'Record', 'Refresh', '', '', 'Save', 'Close')
        for label in buttons:
            if label == '':
                button = QtWidgets.QWidget()
                button_layout.addWidget(button)
                continue
            button = QtWidgets.QPushButton(label)
            button.clicked.connect(self.button_clicked)
            button_layout.addWidget(button)
        return
    
    def button_clicked(self):
        return
    
    def doctor_connect(self):
        return
    
    def update_chat(self):
        return

if __name__ == '__main__':
    a = Main_Window()
    a.show()
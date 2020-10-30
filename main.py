import socket
import threading
from flask import Flask

#####################################
class Server:
    def __init__(self):
            self.ip = socket.gethostbyname(socket.gethostname())
            while 1:
                try:
                    #self.port = int(input('Enter port number to run on --> '))

                    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.s.bind((self.ip, 8090))
                    break
                
                except:
                    print("Couldn't bind to that port")

            self.connections = []
            self.accept_connections()
            

    def accept_connections(self):
        self.s.listen(100)
        print('Running on IP: '+self.ip)
        while True:
            c, addr = self.s.accept()

            self.connections.append(c)

            threading.Thread(target=self.handle_client,args=(c,addr,)).start()
        
    def broadcast(self, sock, data):
        for client in self.connections:
            if client != self.s and client != sock:
                try:
                    client.send(data)
                except:
                    pass
    def handle_client(self,c,addr):
        while 1:
            try:
                data = c.recv(1024)
                self.broadcast(c, data)
            
            except socket.error:
                c.close()

###################################################################
app = Flask(__name__)
@app.route('/start')
def start():
    server = Server()

@app.route('/')
def hello_world():
    nkr = socket.gethostbyname(socket.gethostname())
    return "IP address = %s" %nkr


if __name__ == '__main__':
    app.run()
    

import socket
import threading

class Server:
    def __init__(self):
        self.ip = None
        self.port = None
        self.connections = dict()
        self.doctor = dict()
        self.patient = dict()
        self.server_status = False
        return
    
    def get_port(self):
        while True:
            try:
                self.port = int(input('Enter port number to run on --> '))
            except KeyboardInterrupt:
                print('Stopped server initialization!')
                break
            except:
                print('Please enter integer port!')
                continue
        return
    
    def bind_ip(self):
        try:
            self.ip = socket.gethostbyname(socket.gethostname())
        except:
            print('Socket error!')
            return
        self.get_port()
        if self.port is None: return
        while True:
            try:
                self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.server.bind((self.ip, self.port))
                print('Running on IP: ' + self.ip)
                print('Running on port: '+ str(self.port))
                break
            except:
                print("Couldn't bind to that port.")
                flag = input('Do you want to try again(Y/N)? ')
                if flag.upper() == 'Y':
                    continue
                else:
                    print('Stopped server initialization!')
                    break
        return

    def accept_connections(self):
        self.server_status = True
        self.server.listen(100)
        while self.server_status:
            try:
                conn, addr = self.server.accept()
                verify = conn.recv(2048)
                self.validate_connection(verify, conn, addr)
            except:
                continue
        return
    
    def validate_connection(self, verify, conn, addr):
        return
    
    def start_server(self):
        self.bind_ip()
        self.server_thread= threading.Thread(target=self.accept_connections)
        self.server_thread.start()
        return

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
                data = c.recv(2096)
                self.broadcast(c, data)
            
            except socket.error:
                c.close()

server = Server()

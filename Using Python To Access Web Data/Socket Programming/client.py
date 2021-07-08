import socket
class Client():
    def __init__(self,Adress=(socket.gethostname(),5000)):
        
        self.s = socket.socket()
        self.s.connect(Adress)
        message=self.s.recv(2048)
        print(message.decode("utf-8"))
c = Client()
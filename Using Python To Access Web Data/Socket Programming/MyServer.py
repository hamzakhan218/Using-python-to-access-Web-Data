import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1024))
s.listen(5)
while True:
    clt,adr=s.accept()
    print(f"Connected!!!!  connection to {adr} is established")
    clt.send(bytes("Hamza's Server","utf-8"))
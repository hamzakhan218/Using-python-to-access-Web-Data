import socket, time,os, random

class Server():
  def __init__(self,Adress=(socket.gethostname(),5000),MaxClient=1):
      self.s = socket.socket()
      self.s.bind(Adress)
      self.s.listen(MaxClient)
  def WaitForConnection(self):
      self.Client, self.Adr=(self.s.accept())
      print('Got a connection from: '+str(self.Client)+'.')
      self.Client.send(bytes("Hello this is Hamza's Server","utf-8"))

s = Server()
s.WaitForConnection()
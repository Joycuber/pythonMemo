from socket import socket
from threading import Thread
 
class IncomingThread(Thread):
  def run(self):
    stillChatting = True
    while stillChatting:                     # wait for more incoming data
      transmission = server.recv(1024).decode()       # 'server' will be defined globally at line 27
      lines = transmission.split('\n')[:-1]
      i = 0
      while i < len(lines):
        command = lines[i].split()[0]        # first keyword
        param = lines[i][len(command)+1: ]   # remaining information
        if command == 'GOODBYE':
          stillChatting = False
        elif command == 'NEW':
          print('==> %s has joined the chat room' % param)
        elif command == 'LEFT':
          print('==> %s has left the chat room' % param)
        elif command == 'MESSAGE':
          i += 1                            # need next line for content
          print('==> %s: %s' % (param, lines[i]))
        elif command == 'PRIVATE':
          i += 1                            # need next line for content
          print('==> %s [private]: %s' % (param, lines[i]))
        i += 1

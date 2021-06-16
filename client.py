import socket 
import threading


username = input("Your username: ")


pvariable = 0

class ClientNode:
    def __init__(self):
        self.node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port_and_ip = port_and_ip = ('127.0.0.1', 12008)
        self.node.connect(port_and_ip)

    def send_msg(self, MSG):
        self.node.send(MSG.encode())

    def receive_msg(self):
        while True:       
            data = self.node.recv(1024).decode()
            if data == '':
                pvariable = 2
            else:
                print(data)

    def main(self):
        while True:
            message = input()
            if message == '':
                pvariable = 1
            else:
                self.send_msg(username + ': ' + message)

Client = ClientNode()
always_receive = threading.Thread(target=Client.receive_msg)
always_receive.daemon = True
always_receive.start()
Client.main()
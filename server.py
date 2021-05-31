import socket
import threading

pvariable = 0

username = input("Your username: ")


class ServerNode:
    def __init__(self):
        self.node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port_and_ip = ('127.0.0.1', 12007)
        self.node.bind(port_and_ip)
        self.node.listen(5)
        self.connection, addr = self.node.accept()

    def send_msg(self, MSG):
        self.connection.send(MSG.encode())

    def receive_msg(self):
        while True:
            data = self.connection.recv(1024).decode()
            print(data)

    def main(self):
        while True:
            if message == '':
                pvariable = 1
            else:
                self.send_msg(username + ': ' + message)
server = ServerNode()
always_receive = threading.Thread(target=server.receive_msg)
always_receive.daemon = True
always_receive.start()
server.main()
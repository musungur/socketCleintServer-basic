'''server module.''' 
import socket
# print(dir(socket))

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = '127.0.0.1'
port = 9990
server.bind((host,port))

server.listen(3)
while True:
    # with open('connector','wr') as client:
    client, addr = server.accept()
    print(f"The client: {addr} successfully connected!")
    client.send(f'Dear {addr}, welcome to our services!! We are thrilled to have you connected'.encode('utf-8'))
    cmsg = client.recv(1024).decode('utf-8')
    print(cmsg)
    client.close()
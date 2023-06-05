'''client module.''' 
import socket
host = '127.0.0.1'
port = 9990
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((host,port))

msg = client.recv(1024).decode('utf-8')
print(f'serverMessage:{msg}')
client.send(f'Hi {host}:{port} , thanks for accepting my Connection. I will now use your services'.encode('utf-8'))
client.send(f"I love you{port}".encode('utf-8'))


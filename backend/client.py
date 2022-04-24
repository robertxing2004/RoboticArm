import socket

host = socket.gethostname()
port = 50000

print(socket.gethostname())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((host, port)) # ip and port in tuple

message = server.recv(1024)

print (message.decode("utf-8"))
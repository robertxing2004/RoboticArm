import socket

host = '172.26.139.51'
port = 50001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((host, port)) # ip and port in tuple

while True:
    sent = input("> ").encode()
    server.sendall(sent)
    print("Data successfully sent. Waiting for response")
    
    data = server.recv(1024)
    server.close()
    print (data.decode())

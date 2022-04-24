import socket

print("ok") 

host = socket.gethostname()
port = 50000

print(host)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port)) # ip and port in tuple
server.listen(5)
connection, address = server.accept()
print("Connection established with", address)

while True:
    data = connection.recv(1024)
    if not data: 
        break
    print(data.decode("utf-8")) # Paging Python!
connection.close()

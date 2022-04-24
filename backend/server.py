import socket

host = '127.0.0.1'
port = 50001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port)) # ip and port in tuple
server.listen(5)


connection, address = server.accept()
print("Connection established with", address)

# this section receives the data from processing
while True:
    data = connection.recv(1024)
    data = data.decode()
    if not data: 
        break
    
    if data == "snap":
        print("Taking Pic")

        # after we receive the signal, take a picture, and process it
        # we should get an average x value here
        # send it back to processing 

        xLocation = '100' + '\n'; # send this to processing
        connection.send(xLocation.encode())

connection.close()
        
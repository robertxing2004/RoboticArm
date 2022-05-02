import socket
import cv2
import time
# from color_detection import processImage

# from color_detection import *

averageX = 0

# this function takes the snapshot, very self explanatory
def takeSnapshot():
    img_name = "opencv_frame.png"
    cv2.imwrite(img_name, frame)
    print("snapshot taken")


# setting up the server and looking for a client
host = '127.0.0.1'
port = 50001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port)) # ip and port in tuple
server.listen(5)

connection, address = server.accept()
print("Connection established with", address)

# after there is a client found, opencv turns the camera on
cam = cv2.VideoCapture(0)
cv2.namedWindow("camera")

# ----------------------
# This is the main loop
# ----------------------
while True:

    # looks for a request from the client
    data = connection.recv(1024) # this is like a loop

    # decodes data to ascii
    data = data.decode()
    if not data: 
        break
    
    # if client sends "snap", then read the camera and take a snapshot
    if data == "snap":
        ret, frame = cam.read()
        print("Taking Pic")
        takeSnapshot()
        # processImage()
        
        xLocation = str(averageX) + 'p'; # send this to processing
        connection.send(xLocation.encode())

connection.close()

cam.release()
print("client disconnected")
cv2.destroyAllWindows()
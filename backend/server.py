import socket
import cv2
from time import *
from color_detection import processImage

averageX = 0
newLocation = ""

# ---------------------
# FUNCTIONS FOR PROGRAM
# ---------------------

def takeSnapshot():
    img_name = "RoboticArm/opencv_frame.png"
    cv2.imwrite(img_name, frame)
    print("snapshot taken")

# ---------------------
# SET UP SERVER
# ---------------------

# host = socket.gethostbyname(socket.gethostname())
host  = '127.0.0.1'
port = 50001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

cam = cv2.VideoCapture(0)
cv2.namedWindow("camera")


# ----------------------
# MAIN LOOP
# ----------------------

while True:

    # NO CLIENT CONNECTED
    server.listen(5)
    connection, address = server.accept()
    print("Connection established with", address)

    # CLIENT CONNECTED
    while True:
        data = connection.recv(1024) # this line will loop

        # decodes data to ascii
        data = data.decode()
        if not data: 
            print("client at", address, "has disconnected")
            break
        
        # if client sends "snap", then read the camera and take a snapshot
        if data == "snap":
            ret, frame = cam.read()

            takeSnapshot()
            xLocationInt = processImage()

            xLocation = str(xLocationInt) + 'p'; # send this to processing
            sleep(0.1)
            
            connection.send(xLocation.encode())

            print(xLocation) 

        elif data == "move":
            while newLocation == "":
                newLocation = connection.recv(1024)
            
            newLocation = newLocation.decode()
            
            # this takes newLocation and removes p
            newLocationArray = list(newLocation)
            newLocationArray.pop()

            newLocation = ''

            for i in range(len(newLocationArray)):
                newLocation = newLocation + newLocationArray[i] 

            # call the hardware function here (sean)
            print(newLocation)

            #resets the newLocation variable
            newLocation = ""

connection.close()

cam.release()
print("client disconnected")
cv2.destroyAllWindows()
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

motor1 = (17, 4)
motor2 = (27, 22)
pickupMotor = (10, 9)

GPIO.setup(motor1[0], GPIO.OUT)
GPIO.setup(motor1[1], GPIO.OUT)

currentPos = 0;

def moveLeft(motor):
    GPIO.output(motor[0], False)
    GPIO.output(motor[1], True)
def moveRight(motor):
    GPIO.output(motor[0], True)
    GPIO.output(motor[1], False)
def stop(motor):
    GPIO.output(motor[0], False)
    GPIO.output(motor[1], False)

def PositionToTime(x):
    y = x / 1000
    return y  # float

# Move the arm left (-) or right (+)
def move(pos):
    deltaPos = pos - currentPos

    # Spin motor foreward
    if (deltaPos > 0):  # if x is positive, turn pin 17 on for amount of seconds proportional to x
        moveLeft(motor1)
        moveRight(motor2)
        sleep(PositionToTime(deltaPos))
        stop(motor1)
        stop(motor2)
    # Spin motor backwards
    elif (deltaPos < 0):  # if x is negative, turn pin 4 on for amount of seconds proportional to x
        moveRight(motor1)
        moveLeft(motor2)
        sleep(PositionToTime(deltaPos))
        stop(motor1)
        stop(motor2)

    currentPos = pos

def pickup():
    moveRight(pickupMotor)
    sleep(0.5)
    stop(pickupMotor)
    sleep(0.5)
    moveLeft(pickupMotor)
    sleep(0.5)
    stop(pickupMotor)

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

currentPos = 0;

# Move the arm left (-) or right (+)
def move(pos):
    deltaPos = pos - currentPos

    # Spin motor foreward
    if (deltaPos > 0):  # if x is positive, turn pin 17 on for amount of seconds proportional to x
        GPIO.output(17, True)
        GPIO.output(4, False)
        time.sleep(deltaPos)
        GPIO.output(17, False)
    # Spin motor backwards
    elif (deltaPos < 0):  # if x is negative, turn pin 4 on for amount of seconds proportional to x
        GPIO.output(4, True)
        GPIO.output(17, False)
        time.sleep(deltaPos)
        GPIO.output(4, False)

    currentPos = pos
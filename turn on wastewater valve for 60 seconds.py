#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
# init list with pin numbers
#pinList = [7, 11, 13, 15, 19, 21, 29, 31, 33, 35, 37, 40, 38, 36, 32, 22]
pinList = [32, 29]
# loop through pins and set mode and state to 'low'
for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)
# time to sleep between operations in the main loop
    SleepTimeL = 1200
# main loop
try:
#"Pin #"
    GPIO.output(32, GPIO.LOW)
    GPIO.output(29, GPIO.LOW)
    print ("Emptying Waste Water")
    time.sleep(SleepTimeL);
    GPIO.output(32, GPIO.LOW)
    GPIO.output(29, GPIO.HIGH)
# Reset GPIO settings
    GPIO.cleanup()
    print ("End")
# End program cleanly with keyboard
except KeyboardInterrupt:
    print ("  Quit")

#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
# init list with pin numbers
#pinList = [7, 11, 13, 15, 19, 21, 29, 31, 33, 35, 37, 40, 38, 36, 32, 22]
pinList = [22]
# loop through pins and set mode and state to 'low'
for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)
# time to sleep between operations in the main loop
    SleepTimeL =.01
# main loop
try:
#"Pin #"
    GPIO.output(22, GPIO.LOW)
    print ("Mix Pump On for 10 Minutes")
    time.sleep(SleepTimeL);
    GPIO.output(22, GPIO.HIGH)
# Reset GPIO settings
    GPIO.cleanup()
    print ("End")
# End program cleanly with keyboard
except KeyboardInterrupt:
    print ("  Quit")

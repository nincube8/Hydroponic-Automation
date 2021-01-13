#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# init list with pin numbers

#pinList = [7, 11, 13, 15, 19, 21, 29, 31, 33, 35, 37, 40, 38, 36, 32, 22]
pinList = [7, 11, 13, 15, 19, 21, 29, 31, 33, 35, 37, 40, 38, 36, 32, 22]
# loop through pins and set mode and state to 'low'
for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)
# time to sleep between operations in the main loop
# 
    SleepTimeL =60
# main loop
try:
#"Pin #"
#First Value is the Plant Valve Number, Second number is the Feeding Pump
#Valve 3 Is for Feeding Food Plants and drops water into Cheezits bucket to feed.
#Will cycle through to plant valves 1-6 skipping the 3rd valve
    #Valve 1
    GPIO.output(7, GPIO.LOW)
    GPIO.output(32, GPIO.LOW)
    print ("Feeding Plant Valve 1")
    time.sleep(SleepTimeL);
    GPIO.output(7, GPIO.HIGH)
    GPIO.output(32, GPIO.HIGH)
    #Valve 2
    GPIO.output(11, GPIO.LOW)
    GPIO.output(32, GPIO.LOW)
    print ("Feeding Plant Valve 2")
    time.sleep(SleepTimeL);
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(32, GPIO.HIGH)
    #Valve 4
    GPIO.output(15, GPIO.LOW)
    GPIO.output(32, GPIO.LOW)
    print ("Feeding Plant Valve 4")
    time.sleep(SleepTimeL);
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(32, GPIO.HIGH)
    #Valve 5
    GPIO.output(19, GPIO.LOW)
    GPIO.output(32, GPIO.LOW)
    print ("Feeding Plant Valve 5")
    time.sleep(SleepTimeL);
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(32, GPIO.HIGH)
    #Valve 6
    GPIO.output(21, GPIO.LOW)
    GPIO.output(32, GPIO.LOW)
    print ("Feeding Plant Valve 6")
    time.sleep(SleepTimeL);
    GPIO.output(21, GPIO.HIGH)
    GPIO.output(32, GPIO.HIGH)
    
# Reset GPIO settings
    GPIO.cleanup()
    print ("End")
# End program cleanly with keyboard
except KeyboardInterrupt:
    print ("Quit")

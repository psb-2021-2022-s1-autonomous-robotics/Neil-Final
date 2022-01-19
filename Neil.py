#!/usr/bin/python

import time
import datetime
import RPi.GPIO as GPIO
from Adafruit_LED_Backpack import SevenSegment

#created a varible for the seven second display so I can change it later
segment = SevenSegment.SevenSegment(address=0x70)

# Initialize the display. Must be called once before using the display.
segment.begin()

#Initializing the buzzer
buzzer_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

#tells user how exit program
print("Press CTRL+C to exit")

#asking for time in mintues and seconds for the timer
m = int(input("enter minutes for timer"))
s = int(input("enter seconds for timer"))

# finding total time in seconds
t=m*60+s
print(t)

# Continually update the time on a 4 char, 7-segment display
try:
  while(t>=0):
    
    minute = m
    second = s
    #resting 7 digit display
    segment.clear()
    
    # Set minute on display
    segment.set_digit(0, int(minute / 10))     # Tens
    segment.set_digit(1, minute % 10)          # Ones
    
    # Set seconds on display
    segment.set_digit(2, int(second / 10))   # Tens
    segment.set_digit(3, second % 10)        # Ones

    # update the actual display LEDs.
    segment.write_display()
    
    #if the timer runs out the buzzer buzzes for one second
    if m==0 and s==0:
        GPIO.output(buzzer_pin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(buzzer_pin, GPIO.LOW)
        
    #after setting the display the display waits 1 second before changing again
    time.sleep(1)
    #changes the total time left for timer and removes 1 second from the remaing amount of seconds
    t-=1
    s-=1
    #when a mintue passes, we fix the display and seconds to match real clocks
    if s<0 and m>0:
        m-=1
        s=59
 
# a way to exit the code
except KeyboardInterrupt:
    segment.clear()
    segment.write_display()

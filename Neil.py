#!/usr/bin/python

import time
import datetime
import RPi.GPIO as GPIO
from Adafruit_LED_Backpack import SevenSegment

# ===========================================================================
# Clock Example
# ===========================================================================
segment = SevenSegment.SevenSegment(address=0x70)

# Initialize the display. Must be called once before using the display.
segment.begin()

buzzer_pin = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(buzzer_pin, GPIO.OUT)


print("Press CTRL+C to exit")


m = int(input("enter minutes for timer"))
s = int(input("enter seconds for timer"))


t=m*60+s
print(t)

# Continually update the time on a 4 char, 7-segment display
try:
  while(t>=0):
    minute = m
    second = s
    
    segment.clear()
    # Set minute
    segment.set_digit(0, int(minute / 10))     # Tens
    segment.set_digit(1, minute % 10)          # Ones
    # Set seconds
    segment.set_digit(2, int(second / 10))   # Tens
    segment.set_digit(3, second % 10)        # Ones

    # update the actual display LEDs.
    segment.write_display()
    
    if m==0 and s==0:
        GPIO.output(buzzer_pin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(buzzer_pin, GPIO.LOW)
    # Wait a quarter second (less than 1 second to prevent colon blinking getting$
    time.sleep(1)
    t-=1
    s-=1
    if s<0 and m>0:
        m-=1
        s=59
        
    

except KeyboardInterrupt:
    segment.clear()
    segment.write_display()

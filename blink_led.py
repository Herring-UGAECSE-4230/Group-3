#Variables
freq = 8000
pin = 21

#RPi.GPIO method
import RPi.GPIO as RPI
from time import sleep

#Setup GPIO
RPI.setwarnings(False)
RPI.setmode(RPI.BCM)
RPI.setup(pin, RPI.OUT, initial=RPI.LOW)

half_period = ((1/freq)/2) #calculating sleep times for high and low sections
#Blink the LED
while True:
    RPI.output(pin, RPI.HIGH) #generating square wave
    sleep(half_period)
    RPI.output(pin, RPI.LOW)
    sleep(half_period)


#WiringPi method - WiringPi does not work, remember to document issues in report
# import wiringpi as WPI
# 
# WPI.wiringPiSetupGpio()
# WPI.softToneCreate(pin)
# WPI.softToneWrite(pin, freq)
# 
# while True:
#     #do nothing
#     pass
# WPI.softToneWrite(pin, 0)

#pigpio method
import pigpio

#duty cycle
duty = 127

pi = pigpio.pi()
#setting up frequency and duty cycle
pi.set_PWM_frequency(pin, freq)
pi.set_PWM_dutycycle(pin, duty)

while True:
    #do nothing
    pass
#turn off the square wave
pi.set_PWM_dutycycle(pin, 0)
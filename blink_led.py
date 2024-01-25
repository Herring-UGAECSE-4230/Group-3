#Variables
freq = 1
pin = 21

# #RPi.GPIO method
# import RPi.GPIO as RPI
# from time import sleep
# 
# freq = 10000
# 
# #Setup GPIO
# RPI.setwarnings(False)
# RPI.setmode(RPI.BCM)
# RPI.setup(pin, RPI.OUT, initial=RPI.LOW)
# 
# #Blink the LED
# while True:
#     RPI.output(pin, RPI.HIGH)
#     sleep((1/freq)/2)
#     RPI.output(pin, RPI.LOW)
#     sleep((1/freq)/2)


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




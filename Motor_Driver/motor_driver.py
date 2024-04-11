import RPi.GPIO as RPI

pin_num = 21

RPI.setwarnings(False)
RPI.setmode(RPI.BCM)
RPI.setup(pin_num, RPI.OUT, initial=RPI.LOW)

pwm = RPI.PWM(pin_num, 10) #set frequency
pwm.start(0) #set duty cycle

while True:
  pass

pwm.stop()

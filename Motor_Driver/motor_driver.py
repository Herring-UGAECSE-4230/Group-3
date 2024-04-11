import RPi.GPIO as RPI

pin_num = 21
duty = 0

RPI.setwarnings(False)
RPI.setmode(RPI.BCM)
RPI.setup(pin_num, RPI.OUT, initial=RPI.LOW)

pwm = RPI.PWM(pin_num, 10) #set frequency
pwm.start(duty) #set duty cycle

while True:
  pass

pwm.stop()

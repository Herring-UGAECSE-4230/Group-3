import RPi.GPIO as RPI
pin_num = 5
pwm = RPI.PWM(pin_num, 1000) #1kHz frequency
pwm.start(50) #50% duty cycle

while True:
  pass

pwm.stop()

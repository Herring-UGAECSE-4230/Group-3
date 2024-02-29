from display import display
import RPi.GPIO as rpi
from time import sleep
from queue import Queue

rpi.setwarnings(False)

led_pin = 14 #change to pin used for led

rpi.setmode(rpi.BCM)
rpi.setup(led_pin, rpi.OUT)

def entry(q):
    dp = False
    input = ["0", "0", "0", "0", " "]

    i = 0
    while i < 4:
        while(q.empty()):
            input[i] = ' '
            display(input)
            sleep(.2)
            input[i] = '0'
            display(input)
            sleep(.2)
        
        digit = q.get()

        if i == 0:
            if (digit == "0" or digit == "1" or digit == "2"):
                input[i] = digit
                rpi.output(led_pin, rpi.LOW)
                display(input)
                i += 1
            else:
                rpi.output(led_pin, rpi.HIGH)

        elif i == 1:
            if (input[0] == "0" or input[0] == "1"):
                if (not(digit == "A" or digit == "B" or digit == "C" or digit == "D")):
                    input[i] = digit
                    hour_str = input[0] + input[1]
                    hour = int(hour_str)
                    if (hour >= 12):
                        input[4] = "."
                        if not(hour == 12):
                            hour -= 12
                    hour_str = '{0:02d}'.format(hour)
                    input[0] = hour_str[0]
                    input[1] = hour_str[1]
                    rpi.output(led_pin, rpi.LOW)
                    display(input)
                    i += 1   
                else:
                    rpi.output(led_pin, rpi.HIGH)
            else:
                if (digit == "0" or digit == "1" or digit == "2" or digit == "3"):
                    input[i] = digit
                    hour_str = input[0] + input[1]
                    hour = int(hour_str)
                    if (hour >= 12):
                        input[4] = "."
                        if not(hour == 12):
                            hour -= 12
                    hour_str = '{0:02d}'.format(hour)
                    input[0] = hour_str[0]
                    input[1] = hour_str[1]
                    rpi.output(led_pin, rpi.LOW)
                    display(input)
                    i += 1   
                else:
                    rpi.output(led_pin, rpi.HIGH)

        elif i == 2:
            if (digit == "0" or digit == "1" or digit == "2" or digit == "3" or digit == "4" or digit == "5"):
                input[i] = digit
                rpi.output(led_pin, rpi.LOW)
                display(input)
                i += 1
            else:
                rpi.output(led_pin, rpi.HIGH)
        
        elif i == 3:
            if (not(digit == "A" or digit == "B" or digit == "C" or digit == "D")):
                input[i] = digit
                rpi.output(led_pin, rpi.LOW)
                display(input)
                i += 1
            else:
                rpi.output(led_pin, rpi.HIGH)
            
    return input

from datetime import datetime
from time import sleep
import seven_segment_code
import RPi.GPIO as rpi
from seven_segment_code import pin_list


CLK1 = 16
CLK2 = 9
CLK3 = 10
CLK4 = 11

def auto_clock():

    while True:

        sleep(.25)
        now=datetime.now()
        minute = now.minute
        hour = now.hour

        if hour > 12:
            hour = hour - 12

        clock_string = ('{0:02d}'.format(hour) + '{0:02d}'.format(minute))
        clock_list = [*clock_string]

        

        for i, val in enumerate(clock_list):
            clock = i + 1

            x = str(val)
            seven_segment_code.flip_flop(x)

            if clock == 1:
                rpi.output(CLK1,rpi.HIGH)
                sleep(0.01)
                rpi.output(CLK1,rpi.LOW)
                sleep(0.01)

            elif clock == 2:
                rpi.output(CLK2,rpi.HIGH)
                sleep(0.01)
                rpi.output(CLK2,rpi.LOW)
                sleep(0.01)
                rpi.output(pin_list.LOW)

            elif clock == 3:
                rpi.output(CLK3,rpi.HIGH)
                sleep(0.01)
                rpi.output(CLK3,rpi.LOW)
                sleep(0.01)
                rpi.output(pin_list.LOW)

            elif clock == 4:
                rpi.output(CLK4,rpi.HIGH)
                sleep(0.01)
                rpi.output(CLK4,rpi.LOW)
                sleep(0.01)
                rpi.output(pin_list.LOW)
        
            

auto_clock()

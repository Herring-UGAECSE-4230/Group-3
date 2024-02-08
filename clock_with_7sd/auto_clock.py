from datetime import datetime
from time import sleep
import RPi.GPIO as rpi


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
            digit = val

            if clock == 1:
                rpi.output(CLK1,rpi.HIGH)
                sleep(1/sample_rate)
                rpi.output(CLK1,rpi.LOW)
                sleep(1/sample_rate)

            elif clock == 2:
                rpi.output(CLK2,rpi.HIGH)
                sleep(1/sample_rate)
                rpi.output(CLK2,rpi.LOW)
                sleep(1/sample_rate)
                rpi.output(pin_list.LOW)

            elif clock == 3:
                rpi.output(CLK3,rpi.HIGH)
                sleep(1/sample_rate)
                rpi.output(CLK3,rpi.LOW)
                sleep(1/sample_rate)
                rpi.output(pin_list.LOW)

            elif clock == 4:
                rpi.output(CLK4,rpi.HIGH)
                sleep(1/sample_rate)
                rpi.output(CLK4,rpi.LOW)
                sleep(1/sample_rate)
                rpi.output(pin_list.LOW)
        
            

auto_clock()

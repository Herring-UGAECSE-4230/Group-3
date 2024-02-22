from datetime import datetime
from time import sleep
import seven_segment_code
import RPi.GPIO as rpi
from seven_segment_code import pin_list


CLK1 = 16
CLK2 = 9
CLK3 = 10
CLK4 = 11

CLK_list = [CLK1, CLK2, CLK3, CLK4]

rpi.setmode(rpi.BCM)
rpi.setup(CLK_list, rpi.OUT)

def auto_clock():



    while True:
        
        #gets current time from datetime library
        sleep(.25)
        now=datetime.now()
        minute = now.minute
        hour = now.hour

        #converts clock into 12 hour clock and turns on dot to denote pm
        if hour > 12:
            hour = hour - 12
            dp = True
        else:
            rpi.output(seven_segment_code.DP,rpi.LOW)
            rpi.output(CLK4,rpi.HIGH)
            sleep(0.01)
            rpi.output(CLK4,rpi.LOW)
            sleep(0.01)    

        #making the time into a list of strings
        clock_string = ('{0:02d}'.format(hour) + '{0:02d}'.format(minute))
        clock_list = [*clock_string]

        
        #reads each item in the and pulses its corresponding clock
        for i, val in enumerate(clock_list):
            clock = i + 1

            x = str(val)
            seven_segment_code.flip_flop(x, True, '0', False)

            if clock == 1:
                rpi.output(CLK1,rpi.HIGH)
                sleep(0.01)
                rpi.output(CLK1,rpi.LOW)
                sleep(0.01)
                rpi.output(pin_list, rpi.LOW)

            elif clock == 2:
                rpi.output(CLK2,rpi.HIGH)
                sleep(0.01)
                rpi.output(CLK2,rpi.LOW)
                sleep(0.01)
                rpi.output(pin_list, rpi.LOW)

            elif clock == 3:
                rpi.output(CLK3,rpi.HIGH)
                sleep(0.01)
                rpi.output(CLK3,rpi.LOW)
                sleep(0.01)
                rpi.output(pin_list, rpi.LOW)

            elif clock == 4:
                seven_segment_code.flip_flop(x, True, '0', dp)
                rpi.output(CLK4,rpi.HIGH)
                sleep(0.01)
                rpi.output(CLK4,rpi.LOW)
                sleep(0.01)  
                rpi.output(pin_list, rpi.LOW)      
            


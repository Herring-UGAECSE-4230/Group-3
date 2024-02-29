from time import sleep
import seven_segment_code
import RPi.GPIO as rpi
from seven_segment_code import pin_list

rpi.setwarnings(False)

CLK_list = [16, 9, 10, 11]

rpi.setmode(rpi.BCM)
rpi.setup(CLK_list, rpi.OUT)


def display(output):
        dp = False
        i = 0
        if output[4] == ".":
             dp = True
        while i < 4:
            digit = output[i]
            if i == 1:
                seven_segment_code.flip_flop(output[i], dp)
            else:
                seven_segment_code.flip_flop(output[i], False)
            rpi.output(CLK_list[i],rpi.HIGH)
            sleep(0.01)
            rpi.output(CLK_list[i],rpi.LOW) 
            
            i+=1
from seven_segment_code import flip_flop
import RPi.GPIO as rpi
from time import sleep
from queue import Queue

CLK_list = [0,1,2,3]
CLK_GPIO = [16,9,10,11]



def four_ssd(q):

    while True:

        for i in CLK_list:
            input = q.get()
            flip_flop(input, True, '0', False)
            rpi.output(CLK_GPIO[i],rpi.HIGH)
            sleep(0.01)
            rpi.output(CLK_GPIO[i],rpi.LOW)
            sleep(0.01)

from seven_segment_code import flip_flop
import RPi.GPIO as rpi
from auto_clock import pin_list
from time import sleep
from queue import Queue
from main import input

CLK_list = [1,2,3,4]
CLK_GPIO = [16,9,10,11]



def four_ssd():

    while True:

        for i in CLK_list:

            flip_flop(input)
            rpi.output(CLK_GPIO[i],rpi.HIGH)
            sleep(0.01)
            rpi.output(CLK_GPIO[i],rpi.LOW)
            sleep(0.01)

            i += 1
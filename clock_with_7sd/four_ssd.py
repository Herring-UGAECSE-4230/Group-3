from seven_segment_code import flip_flop
import RPi.GPIO as rpi
from time import sleep
from queue import Queue
from main import prev_state



CLK_list = [0,1,2,3]
CLK_GPIO = [16,9,10,11]
pin_list = [4,27,25,12,13,5,6,26]
led_pin = 1 #change to pin used for led


rpi.setmode(rpi.BCM)
rpi.setup(led_pin, rpi.OUT)




led_state = False

def four_ssd(q):

    while True:

        if led_state == True:
            rpi.output(led_pin, rpi.HIGH)
        elif led_state == False:
            rpi.output(led_pin, rpi.LOW)

        if input != "A"or"B"or"C"or"D":

            led_state = False

            for i in CLK_list:
                input = q.get()
                flip_flop(input, on, prev_state, dp)
                rpi.output(CLK_GPIO[i],rpi.HIGH)
                sleep(0.01)
                rpi.output(CLK_GPIO[i],rpi.LOW)
                sleep(0.01)

        else:
            led_state = True

        
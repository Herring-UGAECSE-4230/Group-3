from seven_segment_code import flip_flop
import RPi.GPIO as rpi
from time import sleep
from queue import Queue

CLK_GPIO = [16,9,10,11]
pin_list = [4,27,25,12,13,5,6,26]
led_pin = 14 #change to pin used for led
prev_states = ["0", "0", "0", "0"]


rpi.setmode(rpi.BCM)
rpi.setup(led_pin, rpi.OUT)


def four_ssd(q):
    output_on = True
    dp = False
    time_string = ""

    i = 0
    while i < 4:
        input = q.get()
        if (input == "A" or input == "B" or input == "C" or input == "D"):
            rpi.output(led_pin, rpi.HIGH)
            print("Bad input")
        else:
            rpi.output(led_pin, rpi.LOW)
            if (input == '#'):
                output_on = not output_on
                for x in range (4):
                    flip_flop(input, output_on, prev_states[x], dp)
                    rpi.output(CLK_GPIO[x],rpi.HIGH)
                    sleep(0.01)
                    rpi.output(CLK_GPIO[x],rpi.LOW)
                    sleep(0.01)
                    time_string += input
            else:
                prev_states[i]= input
            if input == "*":
                dp = True
            flip_flop(input, output_on, prev_states[i], dp)
            rpi.output(CLK_GPIO[i],rpi.HIGH)
            sleep(0.01)
            rpi.output(CLK_GPIO[i],rpi.LOW)
            sleep(0.01)
            dp = False
            i = i + 1
            
    return time_string

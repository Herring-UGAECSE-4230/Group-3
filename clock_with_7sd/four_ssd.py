from seven_segment_code import flip_flop
import RPi.GPIO as rpi
from time import sleep
from queue import Queue



CLK_list = [0,1,2,3]
CLK_GPIO = [16,9,10,11]
pin_list = [4,27,25,12,13,5,6,26]
led_pin = 1 #change to pin used for led
prev_states = ["0", "0", "0", "0"]


rpi.setmode(rpi.BCM)
rpi.setup(led_pin, rpi.OUT)


def four_ssd(q):
    led_state = False
    output_on = True
    dp = False

    while True:

        if led_state == True:
            rpi.output(led_pin, rpi.HIGH)
        elif led_state == False:
            rpi.output(led_pin, rpi.LOW)

            for i in CLK_list:
                input = q.get()
                if input != "A"or"B"or"C"or"D":
                    led_state = False
                else:
                    led_state = True
                    i = i - 1
                if (input == '#'):
                    output_on = not output_on
                    for x in range (4):
                        flip_flop(input, output_on, prev_states[x], dp)
                        rpi.output(CLK_GPIO[x],rpi.HIGH)
                        sleep(0.01)
                        rpi.output(CLK_GPIO[x],rpi.LOW)
                        sleep(0.01)
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

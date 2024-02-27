import keypad
import auto_clock
import seven_segment_code
from queue import Queue
from threading import Thread
from four_ssd import four_ssd
from manual_clock import man_clock

#auto_clock.auto_clock()

q = Queue()

inputThread = Thread(target = keypad.readKeypad, args = (q, ))
inputThread.start()

prev_state = '1'
output_on = True

#print("Calling man clock")
man_clock("1150")

#while True:
    #four_ssd(q)


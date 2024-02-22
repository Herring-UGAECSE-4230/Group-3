import keypad
import auto_clock
import seven_segment_code
from queue import Queue
from threading import Thread
from four_ssd import four_ssd

#auto_clock.auto_clock()

q = Queue()

inputThread = Thread(target = keypad.readKeypad, args = (q, ))
inputThread.start()

prev_state = '1'
output_on = True

four_ssd(q)

while True:
    input = q.get()
    if (input == '#'):
        output_on = not output_on
    else:
        prev_state = input
    #seven_segment_code.flip_flop(input, output_on, prev_state)

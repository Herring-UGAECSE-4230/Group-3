import keypad
from display import display
import auto_clock
from queue import Queue
from threading import Thread
from manual_entry import entry
#from manual_clock import man_clock

#auto_clock.auto_clock()

q = Queue()

inputThread = Thread(target = keypad.readKeypad, args = (q, ))
inputThread.start()

#prev_state = "0000 "
#output_on = True

#main execution
output = ["0", "0", "0", "0", " "]
display(output)
while True:
    entry(q)   


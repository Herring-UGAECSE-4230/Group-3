import keypad
import seven_segment_code
from queue import Queue
from threading import Thread

q = Queue()

inputThread = Thread(target = keypad.readKeypad, args = (q, ))
inputThread.start()

while True:
    input = q.get()
    flip_flop(input)
    print(input + "\n")

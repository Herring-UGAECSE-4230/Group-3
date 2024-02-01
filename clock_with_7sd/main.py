import keypad
from queue import Queue
from threading import Thread

q = Queue()

inputThread = Thread(target = keypad.readKeypad, args = (q, ))
inputThread.start()

while True:
    input = q.get()
    print(input + "\n")

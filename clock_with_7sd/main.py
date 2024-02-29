import keypad
from display import display
from auto_time import auto_time
from increment import increment
from queue import Queue
from threading import Thread
from manual_entry import entry
from time import sleep

q = Queue()

inputThread = Thread(target = keypad.readKeypad, args = (q, ))
inputThread.start()

startup = ["0", "0", "0", "0", " "]
off = [" ", " ", " ", " ", " "]


#main execution
while True:
    startup = ["0", "0", "0", "0", " "]
    display(startup)
    on = True
    input = q.get()
    if input == "A":
        time_string = auto_time()
    elif input == "B":
        time_string = entry(q)
    display(time_string)
    i = 0
    while i < 600:
        if (not q.empty()):
            input = q.get()
            if input == "#":
                on = not(on)
                if on:
                    display(time_string)
                else:
                    display(off)
            elif input == "B":
                input = q.get()
                if input == "B":
                    input = q.get()
                    if input == "B":
                        break
        sleep(.1)
        if i == 599:
            time_string = increment(time_string)
            i = 0
            display(time_string)
        else:
            i += 1

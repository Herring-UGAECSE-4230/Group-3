from queue import Queue
from time import sleep
import RPi.GPIO as rpi

def readKeypad(queue):
    # X values (output) will be GPIO17-GPIO20
    # Y values (input) will be GPIO21-GPIO24
    X_OFFSET = 17
    Y_OFFSET = 21

    #GPIO setup
    rpi.setmode(rpi.BCM) #sets Broadcom pin numbering
    #Setting up x pins as output
    for pin in range(X_OFFSET, X_OFFSET + 4):
        rpi.setup(pin, rpi.OUT, initial=rpi.LOW)
    #Setting up y pins as input
    for pin in range(Y_OFFSET, Y_OFFSET + 4):
        rpi.setup(pin, rpi.IN)
    
    #Setting up initial variables
    x_coord = 0
    y_coord = 0
    sample_rate = 40

    #Look up table for which char values reside at which key locations
    lut = ["1", "2", "3", "A", 
           "4", "5", "6", "B",
           "7", "8", "9", "C",
           "*", "0", "#", "D"]
    
    #Table to store current values of keys, updated on each sample
    key_vals = [0, 0, 0, 0,
                0, 0, 0, 0,
                0, 0, 0, 0,
                0, 0, 0, 0]

    while True:
        sleep(1/sample_rate) #Controlling the sampling rate of the peripheral
        rpi.output(x_coord + X_OFFSET, rpi.HIGH)
        
        #Reading each Y level
        for y_coord in range(4):
            #Is the current key pressed?
            if rpi.input(y_coord + Y_OFFSET):
                #If so, was the key pressed last time?
                if (key_vals[(x_coord * 4) + y_coord] != 1):
                    #If the level has changed, push the char at that key to the queue 
                    queue.put(lut[(x_coord * 4) + y_coord])
                #Update the current value of the key in the table
                key_vals[(x_coord * 4) + y_coord] = 1
            
            else:
                #Update the current value of the key in the table
                key_vals[(x_coord * 4) + y_coord] = 0

        rpi.output(x_coord + X_OFFSET, rpi.LOW)
        
        #Iterating the row
        if x_coord == 3:
            x_coord = 0
        else:
            x_coord += 1
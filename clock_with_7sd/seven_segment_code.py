import RPi.GPIO as rpi
from time import sleep

pin_list = [4,27,25,12,13,5,6,26]

rpi.setmode(rpi.BCM)
rpi.setup(pin_list, rpi.OUT)

#declaring gpio outputs
a = 4
b = 27
c = 25
d = 12
e = 13
f = 5
g = 6
DP = 26
CLK = 16

rpi.setup(CLK, rpi.OUT)

#setting seven segment values
one = [f,e]
two = [a,b,g,e,d]
three = [a,b,g,c,d]
four = [f,g,b,c]
five = [a,f,g,c,d]
six = [a,c,d,e,f,g]
seven = [a,b,c]
eight = [a,b,c,d,e,f,g]
nine = [a,b,c,d,f,g]
zero = [a,b,c,d,e,f]
A = [a,b,c,e,f,g]
B = [c,d,e,f,g]
C = [a,d,e,f]
D = [b,c,d,e,g]


def flip_flop(input, dp):
        #sending values to flip flop
        if input == " ":
                rpi.output(pin_list, rpi.LOW)

        if input == "1":
                rpi.output(pin_list, rpi.LOW)
                rpi.output(one, rpi.HIGH)
                
        elif input == "2":
                rpi.output(pin_list, rpi.LOW)
                rpi.output(two, rpi.HIGH)

        elif input == "3":
                rpi.output(pin_list, rpi.LOW)
                rpi.output(three, rpi.HIGH)
        
        elif input == "4":
                rpi.output(pin_list, rpi.LOW)
                rpi.output(four, rpi.HIGH)

        elif input == "5":
                rpi.output(pin_list, rpi.LOW)
                rpi.output(five, rpi.HIGH)

        elif input == "6":
                rpi.output(pin_list, rpi.LOW)
                rpi.output(six, rpi.HIGH)

        elif input == "7":
                rpi.output(pin_list, rpi.LOW)
                rpi.output(seven, rpi.HIGH)

        elif input == "8":
                rpi.output(pin_list, rpi.LOW)
                rpi.output(eight, rpi.HIGH)
        
        elif input == "9":
                rpi.output(pin_list, rpi.LOW)
                rpi.output(nine, rpi.HIGH)

        elif input == "0":
                rpi.output(pin_list, rpi.LOW)
                rpi.output(zero, rpi.HIGH)

        elif input == "A":
                rpi.output(pin_list, rpi.LOW)
                rpi.output(A, rpi.HIGH)

        elif input == "B":
                rpi.output(pin_list, rpi.LOW)
                rpi.output(B, rpi.HIGH)

        elif input == "C":
                rpi.output(pin_list, rpi.LOW)
                rpi.output(C, rpi.HIGH)
        
        elif input == "D":
                rpi.output(pin_list, rpi.LOW)
                rpi.output(D, rpi.HIGH)
        
        if dp:
                rpi.output(DP, rpi.HIGH)

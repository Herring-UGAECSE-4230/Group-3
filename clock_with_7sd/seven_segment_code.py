import RPi.GPIO as rpi
from time import sleep



pin_list = [4,27,25,12,13,5,6,26]

rpi.setmode(pin_list, rpi.OUT)

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
B = [a,b,c,d,e,f,g,DP]
C = [a,d,e,f]
D = [a,b,c,d,e,f,DP]


def flip_flop(x):
        
        
#sending values to flip flop
        if x == "1":
                rpi.output(pin_list.LOW)
                rpi.output(one, rpi.HIGH)
                
        elif x == "2":
                rpi.output(pin_list.LOW)
                rpi.output(two, rpi.HIGH)

        elif x == "3":
                rpi.output(pin_list.LOW)
                rpi.output(three, rpi.HIGH)
        
        elif x == "4":
                rpi.output(pin_list.LOW)
                rpi.output(four, rpi.HIGH)

        elif x == "5":
                rpi.output(pin_list.LOW)
                rpi.output(five, rpi.HIGH)

        elif x == "6":
                rpi.output(pin_list.LOW)
                rpi.output(six, rpi.HIGH)

        elif x == "7":
                rpi.output(pin_list.LOW)
                rpi.output(seven, rpi.HIGH)

        elif x == "8":
                rpi.output(pin_list.LOW)
                rpi.output(eight, rpi.HIGH)
        
        elif x == "9":
                rpi.output(pin_list.LOW)
                rpi.output(nine, rpi.HIGH)

        elif x == "0":
                rpi.output(pin_list.LOW)
                rpi.output(zero, rpi.HIGH)

        elif x == "A":
                rpi.output(pin_list.LOW)
                rpi.output(A, rpi.HIGH)

        elif x == "B":
                rpi.output(pin_list.LOW)
                rpi.output(B, rpi.HIGH)

        elif x == "C":
                rpi.output(pin_list.LOW)
                rpi.output(C, rpi.HIGH)
        
        elif x == "D":
                rpi.output(pin_list.LOW)
                rpi.output(D, rpi.HIGH)
        elif x == "#":
                rpi.output(pin_list.LOW)
                rpi.output(g, rpi.HIGH)
        
        elif x == "*":
                rpi.output(pin_list.LOW)
                rpi.output(DP, rpi.HIGH)

#        rpi.output(CLK,rpi.HIGH)
#       sleep(1/sample_rate)
#        rpi.output(CLK,rpi.LOW)
#        sleep(1/sample_rate)
#        rpi.output(pin_list.LOW)
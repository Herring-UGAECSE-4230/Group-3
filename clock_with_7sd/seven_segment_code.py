x = input(rpi.output(x_coord + X_OFFSET, rpi.LOW))
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

#sending values to flip flop
match x:
    case "1":
       rpi.output(pin_list.LOW)
       rpi.output(one, rpi.HIGH) 

    case "2":
        rpi.output(pin_list.LOW)
        rpi.output(two, rpi.HIGH)

    case "3":
        rpi.output(pin_list.LOW)
        rpi.output(three, rpi.HIGH)
    
    case "4":
        rpi.output(pin_list.LOW)
        rpi.output(four, rpi.HIGH)

    case "5":
        rpi.output(pin_list.LOW)
        rpi.output(five, rpi.HIGH)

    case "6":
        rpi.output(pin_list.LOW)
        rpi.output(six, rpi.HIGH)

    case "7":
        rpi.output(pin_list.LOW)
        rpi.output(seven, rpi.HIGH)

    case "8":
        rpi.output(pin_list.LOW)
        rpi.output(eight, rpi.HIGH)
    
    case "9":
        rpi.output(pin_list.LOW)
        rpi.output(nine, rpi.HIGH)

    case "0":
        rpi.output(pin_list.LOW)
        rpi.output(zero, rpi.HIGH)

    case "A":
        rpi.output(pin_list.LOW)
        rpi.output(A, rpi.HIGH)

    case "B":
        rpi.output(pin_list.LOW)
        rpi.output(B, rpi.HIGH)

    case "C":
        rpi.output(pin_list.LOW)
        rpi.output(C, rpi.HIGH)
    
    case "D":
        rpi.output(pin_list.LOW)
        rpi.output(D, rpi.HIGH)

    case "#":
        rpi.output(pin_list.LOW)
        rpi.output(DP, rpi.HIGH)
   
    case "*":
        rpi.output(pin_list.LOW)
        rpi.output(*, rpi.HIGH)

    case _:
        rpi.output(pin_list, rpi.LOW)

import RPi.GPIO as RPI
from time import sleep
import numpy as np

codes_dict = {'A':'. - ', 'B':'- . . .', 'C':'- . - .', 'D':'- . .', 'E':'.',
'F':'. . - .', 'G':'- - . ', 'H':'. . . .', 'I':'. .', 'J':'. - - -', 'K':'- . -',
'L':'. - . .', 'M':'- -', 'N':'- .', 'O':'- - -', 'P':'. - - .', 'Q':'- - . -',
'R':'. - .', 'S':'. . .', 'T':'-', 'U':'. . -', 'V':'. . . -', 'W':'. - -',
'X':'- . . -', 'Y':'- . - -', 'Z':'- - . .', '1':'. - - - -', '2':'. . - - -', '3':'. . . - -',
'4':'. . . . -', '5':'. . . . .', '6':'- . . . .', '7':'- - . . .', '8':'- - - . .', '9':'- - - - .',
'0':'- - - -  -' }


with open(r'MorseCode.txt') as file: #replace with pi path
    lines = [line for line in file.readlines()]
translation = '- . - . - | ATTENTION \n'
file.close()
for message in lines:
    i = 0
    message = message.upper()
    word = message.split()
    for letter in message:
        code = str(codes_dict.get(letter))
        if code == 'None':
            translation += ' | ' + word[i] + '\n'
            i += 1
        else:
            translation += code + '   ' 
    translation += '- . - | OVER \n' 
print (translation)

#Setup GPIO
pinList = [5,6]
freq = 1000
RPI.setwarnings(False)
RPI.setmode(RPI.BCM)
RPI.setup(pinList, RPI.OUT, initial=RPI.LOW)
half_period = ((1/freq)/2) #calculating sleep times for high and low sections

<<<<<<< HEAD
# for c in translation:
#     if c == '.':
#         for x in range(250):
#             RPI.output(pinList, RPI.HIGH) #generating square wave
#             sleep(half_period)
#             RPI.output(pinList, RPI.LOW)
#             sleep(half_period)
#         
#     elif c == '-':
#         for x in range(750):
#             RPI.output(pinList, RPI.HIGH) #generating square wave
#             sleep(half_period)
#             RPI.output(pinList, RPI.LOW)
#             sleep(half_period)
# 
#     elif c == ' ':
#         sleep(.25)
#         
#     elif c == '|':
#         sleep(1.5)
=======
for c in translation:
    if c == '.':
        for x in range(200):
            RPI.output(pin, RPI.HIGH) #generating square wave
            sleep(half_period)
            RPI.output(pin, RPI.LOW)
            sleep(half_period)
        
    elif c == '-':
        for x in range(400):
            RPI.output(pin, RPI.HIGH) #generating square wave
            sleep(half_period)
            RPI.output(pin, RPI.LOW)
            sleep(half_period)

    elif c == '|':
        sleep(.5)
>>>>>>> 35f218a5a9635747c4ed9b11328d6a8f44dbe298

f = open('encoded_message.txt', 'w')
f.write(translation)
f.close()

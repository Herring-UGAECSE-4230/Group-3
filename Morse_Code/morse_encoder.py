import RPi.GPIO as rpi
from time import sleep
import numpy as np

codes_dict = {'A':'. - ', 'B':'- . . .', 'C':'- . - .', 'D':'- . .', 'E':'.',
'F':'. . - .', 'G':'- - . ', 'H':'. . . .', 'I':'. .', 'J':'. - - -', 'K':'- . -',
'L':'. - . .', 'M':'- -', 'N':'- .', 'O':'- - -', 'P':'. - - .', 'Q':'- - . -',
'R':'. - .', 'S':'. . .', 'T':'-', 'U':'. . -', 'V':'. . . -', 'W':'. - -',
'X':'- . . -', 'Y':'- . - -', 'Z':'- - . .', '1':'. - - - -', '2':'. . - - -', '3':'. . . - -',
'4':'. . . . -', '5':'. . . . .', '6':'- . . . .', '7':'- - . . .', '8':'- - - . .', '9':'- - - - .',
'0':'- - - -  -' }


with open(r'C:\Users\jorda\Desktop\Embedded I\Group-3\Morse_Code\MorseCode.txt') as file: #replace with pi path
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
pin = 5
freq = 1000
RPI.setwarnings(False)
RPI.setmode(RPI.BCM)
RPI.setup(pin, RPI.OUT, initial=RPI.LOW)
half_period = ((1/freq)/2) #calculating sleep times for high and low sections

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

    elif c = '|':
        sleep(.5)

f = open('encoded_message.txt', 'w')
f.write(translation)
f.close()

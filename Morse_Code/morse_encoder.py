#import RPi.GPIO as rpi
from time import sleep
import numpy as np

codes_dict = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-',
'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-',
'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--',
'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--',
'4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
'0':'-----', }


with open(r'C:\Users\jorda\Desktop\Embedded I\Group-3\Morse_Code\MorseCode.txt') as file:#replace with pi path
    lines = [line for line in file.readlines()]

translation = ''
print (lines)
for code in lines:
   for char, morse in codes_dict.items():
        if morse == code:
            translation  += char

#        print(translation)

#file.close()
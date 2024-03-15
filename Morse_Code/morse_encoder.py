#import RPi.GPIO as rpi
from time import sleep
import numpy as np

codes_dict = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-',
'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-',
'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--',
'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--',
'4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
'0':'-----', 'attention':'-.-.-'}


with open(r'C:\Users\jorda\Desktop\Embedded I\Group-3\Morse_Code\MorseCode.txt') as file:#replace with pi path
    lines = [line for line in file.readlines()]

translation = ''


for word in lines:
    word = word.upper()
    for letter in word:
        code = str(codes_dict.get(letter))
        if code == 'None':
            translation += '\n '
        else:
            translation += code
            translation += ' ' 

       

print (translation)
        
            


file.close()
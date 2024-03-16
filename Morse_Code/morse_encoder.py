#import RPi.GPIO as rpi
from time import sleep
import numpy as np

codes_dict = {'ATTENTION':'- . - . -', 'A':'. - ', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-',
'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-',
'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--',
'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--',
'4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
'0':'-----' }


with open(r'C:\Users\jorda\Desktop\Embedded I\Group-3\Morse_Code\MorseCode.txt') as file:#replace with pi path
    lines = [line for line in file.readlines()]

translation = ''
file.close()

for word in lines:
    word = word.upper()
    prosign = str(codes_dict.get(word))
    if word == prosign:
        translation += prosign
        translation += ' '
    else:
        for letter in word:
            code = str(codes_dict.get(letter))
            if code == 'None':
                translation += ' | ' + word + '\n'
            else:
                translation += code + ' '       

print (translation)
        
            



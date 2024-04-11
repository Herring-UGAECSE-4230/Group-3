import RPi.GPIO as GPIO
import time

#global variables which can be used from the callback function
global KEY_PRESSED 
global IS_TRAINING
global TRAINING_INDEX
global DOT_LENGTH
global CURRENT_CHAR
global CURRENT_WORD
global codes_dict

IS_TRAINING = False
end_time = time.time()
KEY_PRESSED = False
KEY_GPIO = 21
DOT_LENGTH = 0
TRAINING_INDEX = 0
CURRENT_CHAR = ""
CURRENT_WORD = ""

#dictionary of morse code letters
codes_dict = {'- . - . - ':"Attention", ". - . - . - . - ":"Over",
'. - ':'A', '- . . . ':'B','- . - . ':'C','- . . ':'D', '. ':'E',
'. . - . ':'F', '- - . ':'G', '. . . . ':'H', '. . ':'I', '. - - - ':'J', '- . - ':'K',
'. - . . ':'L', '- - ':'M', '- . ':'N', '- - - ':'O', '. - - . ':'P', '- - . - ':'Q',
'. - . ':'R', '. . . ':'S', '- ':'T', '. . - ':'U', '. . . - ':'V', '. - - ':'W',
'- . . - ':'X', '- . - - ':'Y', '- - . . ':'Z', '. - - - - ':'1', '. . - - - ':'2', '. . . - - ':'3',
'. . . . - ':'4', '. . . . . ':'5', '- . . . . ':'6', '- - . . . ':'7', '- - - . . ':'8', '- - - - . ':'9',
'- - - -  - ':'0' }

#Executes on key press
def start_timer():
    global pwm
    pwm.start(50) # turns on speaker/LED
    global start_time
    start_time = time.time() #Recording time that key press began
    global space
    space = start_time - end_time

def stop_timer():
    global pwm
    pwm.start(0) #Turning off speaker/LED
    file = open('decoded.txt', 'a') #Opening file to append decoded text
    global end_time #recording time that key press ends
    end_time = time.time()
    global length
    length = end_time - start_time #calculating length of key press
    global IS_TRAINING
    global TRAINING_INDEX
    global DOT_LENGTH
    global CURRENT_CHAR
    global CURRENT_WORD
    global codes_dict
    if IS_TRAINING: #determines dot length if program is in training mode
        if (TRAINING_INDEX == 1) or (TRAINING_INDEX == 3):
            DOT_LENGTH += length
        if TRAINING_INDEX == 4:
            IS_TRAINING = False
            DOT_LENGTH = DOT_LENGTH / 2
            print("Dot length is :" + str(DOT_LENGTH))
        else:
            TRAINING_INDEX += 1
    else: #Determines dot/dash, letter, or word spacing and performs decoding
        if (space <= DOT_LENGTH * 6) and (space >= DOT_LENGTH * 3): # for space between letters
            print("  ", end="")
            file.write("   ")
            char = codes_dict.get(str(CURRENT_CHAR))
            if char == None:
                char = "?"
            CURRENT_WORD += char
            CURRENT_CHAR = ""
        elif space >= DOT_LENGTH * 7: #for space between words
            print(" | ", end="")
            file.write(" | ")
            char = codes_dict.get(str(CURRENT_CHAR))
            if char == None:
                char = "?"
            CURRENT_WORD += char
            CURRENT_CHAR = ""
            print(CURRENT_WORD)
            file.write(CURRENT_WORD + '\n')
            CURRENT_WORD = ""
        if length <= DOT_LENGTH * 2: #for dot
            CURRENT_CHAR += ". "
            print(". ", end="")
            file.write(". ")
        else: #for dash
            CURRENT_CHAR += "- "
            print("- ", end="")
            file.write("- ")
    file.close()

def key_pressed_callback(channel): #callback, determines if key is pressed or released
    global KEY_PRESSED
    KEY_PRESSED = not(KEY_PRESSED)
    if KEY_PRESSED:
        start_timer()
    else:
        stop_timer()

if __name__ == '__main__':
    #RPi.GPIO setup
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(KEY_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)
    
    global pwm
    pwm = GPIO.PWM(20, 320) #set frequency
    
    #interrupt event
    GPIO.add_event_detect(KEY_GPIO, GPIO.BOTH, callback=key_pressed_callback, bouncetime=25)
    
    IS_TRAINING = True
    print("Please sign \"Attention\": - . - . -")
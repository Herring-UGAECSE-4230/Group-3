import RPi.GPIO as GPIO
import time

# Define GPIO pins for the encoder
pin_a = 25
pin_b = 24
btn = 23

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_a, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin_b, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Variables to track encoder state and debouncing
last_state_a = GPIO.input(pin_a)
last_state_b = GPIO.input(pin_b)
last_state_btn = GPIO.input(btn)

debounce_delay = 0.001

try:
    while True:

        # Read current state of pins
        state_a = GPIO.input(pin_a)
        state_b = GPIO.input(pin_b)
        btn_state = GPIO.input(btn)
        
        # Debouncing
        if state_a != last_state_a or state_b != last_state_b or btn_state != last_state_btn:
            time.sleep(debounce_delay)
            state_a = GPIO.input(pin_a)
            state_b = GPIO.input(pin_b)
            btn_state = GPIO.input(btn)
        
        # Check for changes in encoder state
        if state_a != last_state_a or state_b != last_state_b:
            if state_a != last_state_a:
                if state_a != state_b:
                    print('cw')
                else:
                    print('ccw')
        
        if btn_state != last_state_btn and btn_state == True:
            print('button pressed')

        
        # Update last state
        last_state_a = state_a
        last_state_b = state_b
        last_state_btn = btn_state
        # Small delay to save CPU cycles
        time.sleep(0.001)

finally:
    GPIO.cleanup()

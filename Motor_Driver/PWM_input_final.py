import RPi.GPIO as GPIO
import time

# Define GPIO pins for the encoder
pin_a = 17
pin_b = 18

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_a, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin_b, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Variables to track encoder state and debouncing
last_state_a = GPIO.input(pin_a)
last_state_b = GPIO.input(pin_b)
debounce_delay = 0.01  # Adjust as necessary

try:
    while True:
        # Read current state of pins
        state_a = GPIO.input(pin_a)
        state_b = GPIO.input(pin_b)
        
        # Debouncing
        if state_a != last_state_a or state_b != last_state_b:
            time.sleep(debounce_delay)
            state_a = GPIO.input(pin_a)
            state_b = GPIO.input(pin_b)
        
        # Check for changes in encoder state
        if state_a != last_state_a or state_b != last_state_b:
            if state_a != last_state_a:
                print("Encoder A changed")
            if state_b != last_state_b:
                print("Encoder B changed")
        
        # Update last state
        last_state_a = state_a
        last_state_b = state_b
        
        # Small delay to save CPU cycles
        time.sleep(0.001)

finally:
    GPIO.cleanup()

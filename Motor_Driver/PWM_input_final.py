import RPi.GPIO as GPIO
import time

def inc_counter(channel):
    global counter
    counter += 1
    
def rpm_to_duty(rpm):
    if (rpm < 400):
        return 0
    elif (rpm >= 400 and rpm < 700):
        return ((rpm - 400)/10)
    elif (rpm >= 700 and rpm < 1200):
        return (((rpm - 700)/50) + 30)
    elif (rpm >= 1200):
        return (((rpm - 1200)/20) + 40)
    else:
        return 100
if __name__ == '__main__':
    # Define GPIO pins for the encoder
    pin_a = 25
    pin_b = 24
    btn = 23
    pin_num = 21
    set_rpm = 0
    duty = 0.0001
    prev_rpm = 0


    # Setup GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_a, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(pin_b, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # Variables to track encoder state and debouncing
    last_state_a = GPIO.input(pin_a)
    last_state_b = GPIO.input(pin_b)
    last_state_btn = GPIO.input(btn)

    global prev_time
    prev_time = time.time()
    global counter
    counter = 0
    
    debounce_delay = 0.001

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_num, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    pwm = GPIO.PWM(pin_num, 10000) #set frequency
    pwm.start(duty) #set duty cycle
    #interrupt event
    GPIO.add_event_detect(20, GPIO.RISING, callback=inc_counter, bouncetime=10)

    try:
        while True:
            current_time = time.time()
            if ((current_time - prev_time) >= 1):
                rotations = counter/3
                rps = rotations/(current_time - prev_time)
                rpm = rps * 60
                prev_time = current_time
                print("Actual RPM: " + str(rpm))
                counter = 0
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
                        if set_rpm < 1800:
                            set_rpm += 25
                        print("Expected RPM: " + str(set_rpm))
                        pwm.start(rpm_to_duty(set_rpm))
                    else:
                        if set_rpm > 400:
                            set_rpm -= 25
                        print("Expected RPM: " + str(set_rpm))
                        pwm.start(rpm_to_duty(set_rpm))
        
            if btn_state != last_state_btn and btn_state == True:
                print('button pressed')
                if set_rpm > 0:
                    prev_rpm = set_rpm
                    set_rpm = 0
                    print("Expected RPM: " + str(set_rpm))
                    pwm.start(rpm_to_duty(set_rpm))
                else:
                    set_rpm = prev_rpm
                    print("Expected RPM: " + str(set_rpm))
                    pwm.start(rpm_to_duty(set_rpm))

            # Update last state
            last_state_a = state_a
            last_state_b = state_b
            last_state_btn = btn_state
            # Small delay to save CPU cycles
            time.sleep(0.001)

    finally:
        GPIO.cleanup()

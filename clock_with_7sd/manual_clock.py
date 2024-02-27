from time import sleep
import seven_segment_code
import RPi.GPIO as rpi
from seven_segment_code import pin_list

rpi.setwarnings(False)

CLK1 = 16
CLK2 = 9
CLK3 = 10
CLK4 = 11

CLK_list = [CLK1, CLK2, CLK3, CLK4]

dp = False

rpi.setmode(rpi.BCM)
rpi.setup(CLK_list, rpi.OUT)


def man_clock(time_string):
    print("in man clock")

    hour = int (time_string[:2])
    minute = int (time_string[2:])
 
    while True:  

        if hour > 12:
            hour = hour -12
            dp = True
        else:
            dp = False
            #rpi.output(seven_segment_code.DP,rpi.LOW)
            #rpi.output(CLK4,rpi.HIGH)
            #sleep(0.01)
            #rpi.output(CLK4,rpi.LOW)
            #sleep(0.01)    
        time_string = ('{0:02d}'.format(hour) + '{0:02d}'.format(minute))
        print ("Time string: " + time_string)

        i = 0
        while i < 4:

            output = time_string[i]
            if i < 3:
                seven_segment_code.flip_flop(output, True, '0', False)
            else:
                seven_segment_code.flip_flop(output, True, '0', dp)
            rpi.output(CLK_list[i],rpi.HIGH)
            sleep(0.01)
            rpi.output(CLK_list[i],rpi.LOW) 
            
            i+=1

        sleep(10)

        if minute < 59:
            minute += 1

        else:
            minute = 0
            hour += 1
                

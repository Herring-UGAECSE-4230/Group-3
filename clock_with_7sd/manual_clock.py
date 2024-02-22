from time import sleep
#from four_ssd import time_string


time_string = "1650"

def man_clock(time_string):

    hour = int (time_string[:2])
    min = int (time_string[2:])

    while True:

   
        sleep(1)
        if hour > 12:
                hour = hour -12

        if min < 59:
             min += 1

        else:
            min = 0
            hour += 1
            
                

        print('{0:02d}'.format(hour) +":"+ '{0:02d}'.format(min))

man_clock(time_string)
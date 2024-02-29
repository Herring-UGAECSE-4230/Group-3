from datetime import datetime

def auto_time():
        
        #gets current time from datetime library
        now=datetime.now()
        minute = now.minute
        hour = now.hour
        dp = False

        #converts clock into 12 hour clock and turns on dot to denote pm
        if hour >= 12:
            dp = True
            if not (hour == 12):
                hour -= 12

        #making the time into a list of strings
        time_string = ('{0:02d}'.format(hour) + '{0:02d}'.format(minute))
        if dp:
            time_string += '.'
        else:
            time_string += ' '

        return time_string

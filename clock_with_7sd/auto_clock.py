from datetime import datetime

def auto_clock():
    while True:
        now=datetime.now()
        minute = now.minute
        hour = now.hour

        if hour > 12:
            hour = hour - 12

        
        print('{0:02d}'.format(hour), ":", '{0:02d}'.format(minute))



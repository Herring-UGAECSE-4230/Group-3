from datetime import datetime

def auto_clock():
    while True:
        now=datetime.now()
        minute = now.minute
        hour = now.hour

        if hour > 12:
            hour = hour - 12

        ssd_h = '{0:02d}'.format(hour)
        ssd_m = '{0:02d}'.format(minute)

        print(ssd_h, ":", ssd_m)
        
auto_clock()

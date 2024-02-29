def increment(time_string):
    
    pm = False
    if time_string[4] == ".":
        pm = True

    hour = int (time_string[0] + time_string[1])
    minute = int (time_string[2] + time_string[3])

    #iterates a minute
    minute += 1
    #calculating rollover for 59->60 mins
    if minute > 59:
        hour += 1
        minute = 0
    
    #calculating rollover for 12->13 hrs and am/pm
    if hour > 12:
        hour -= 12
        pm = not(pm)
 
    #formatting new time string
    time_string = ["","","","",""]
    hour_str = '{0:02d}'.format(hour)
    time_string[0] = hour_str[0]
    time_string[1] = hour_str[1]

    minute_str = '{0:02d}'.format(minute)
    time_string[2] = minute_str[0]
    time_string[3] = minute_str[1]

    if pm:
        time_string[4] = '.'
    else:
        time_string[4] = ' '

    return time_string
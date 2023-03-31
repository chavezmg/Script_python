def add_time(start, duration, day=0):
    if ":" in start:
        separator_index = start.index(":")
    if "AM" in start:
        start_index = start.index(" AM")
        time_adjust = 0
    elif "PM" in start:
        start_index = start.index(" PM")
        time_adjust = 12
    if ":" in duration:
        duration_index = duration.index(":")
        durationFp = int(duration[:duration_index])
        durationSp = int(duration[duration_index+1:])

    startFp = int(start[:separator_index]) + time_adjust  #first part of the number (number before :)
    startSp = int(start[separator_index+1:start_index])   #second part of the number (number after :)
    durationTime = durationFp*60 + durationSp         #duration time in minutes
    startTime = startFp*60 + startSp        #get the whole start time in minutes
    resultTime = startTime + durationTime   #final time to return, in minutes

    days = int(resultTime/1440)                  #days to return
    hours = int((resultTime%1440)/60)
    minutes = int((resultTime%1440)%60)

    ##here we convert days, hours and minutes to formatted strings   
    days = str(days) 
    if hours < 12:
        if hours == 00:
            hours = "12"
        else:
            hours = str(hours)
        if minutes < 10:
            minutes = ":" + "0" + str(minutes) + " AM"
        else:
            minutes = ":" + str(minutes) + " AM"
    elif hours>=12:
        hours -= 12
        if hours == 00:
            hours = "12"
        else:
            hours = str(hours)   
        if minutes < 10:
            minutes = ":" + "0" +str(minutes) + " PM"
        else:
            minutes = ":" + str(minutes) + " PM"
    ## end formatting
    
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    ## here we return the values for the different cases
    if day == 0:
        if(resultTime < 1440):
            return hours + minutes
        elif(resultTime >= 1440 and resultTime < 2880):
            return hours + minutes + " (next day)"
        elif(resultTime >= 2880):
            return hours + minutes + f" ({days} days later)"
    else:
        day = day.lower()
        day = day.capitalize()
        day_index = week_days.index(day)
        if(resultTime < 1440):
            return hours + minutes + f", {day}"
        elif(resultTime >= 1440):
            day = int(days) + day_index
            if day > 6:
                day = day%7
            if int(days) > 1:
                return hours + minutes + f", {week_days[day]}" + f" ({days} days later)"   
            else: 
                return hours + minutes + f", {week_days[day]}" + " (next day)"

    ##end return values

print(add_time("8:16 PM", "466:02", "tuesday"))
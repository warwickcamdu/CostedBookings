from parse_events import calculate_time
import iso8601

def cost_hours(events):

    for i in range(len(events)):
        event = events[i]
        print(event)
        time_start = iso8601.parse_date(event[2])
        time_end = iso8601.parse_date(event[3])
        hours = 0
        #overnight
        if time_start.day != time_end.day:
            print("overnight")
            #check that it is mon-thu
            if time_start.weekday() < 4:
                #at least 4h
                print("weekday")
                hours = min(4.0, calculate_time(event[2],event[3]).total_seconds()/3600.0)
                #calculate time before 18h
                startts = event[2][:10]+"T18:00:00Z"
                extra = max(0.0,calculate_time(event[2],startts).total_seconds()/3600.0)
                print(str(extra)+" extra hours")
                hours = hours + extra
                #calculate time after 9h
                endts = event[3][:10]+"T09:00:00Z"
                extra = max(0.0,calculate_time(endts,event[3]).total_seconds()/3600.0)
                print(str(extra)+" extra hours")
                hours = hours + extra
            #check for friday start
            elif time_start.weekday() == 4:
                print("Friday")
                hours = min(4.0, calculate_time(event[2],event[3]).total_seconds()/3600.0)
                #calculate time before 18h
                startts = event[2][:10]+"T18:00:00Z"
                extra = max(0.0,calculate_time(event[2],startts).total_seconds()/3600.0)
                print(str(extra)+" extra hours")
                hours = hours + extra
            #check for sunday start
            elif time_start.weekday() == 6:
                hours = 0
                print("Sunday")
                #calculate time after 9h
                endts = event[3][:10]+"T09:00:00Z"
                extra = max(0.0,calculate_time(endts,event[3]).total_seconds()/3600.0)
                print(str(extra)+" extra hours")
                hours = hours + extra
        else:
            print("regular")
            hours = calculate_time(event[2],event[3]).total_seconds()/3600.0
            if time_end.hour > 21:
                startts = event[2][:10]+"T18:00:00Z"
                extra = max(0.0,calculate_time(event[2],startts).total_seconds()/3600.0)
                hours = 4.0 + extra
            if time_start.hour < 5:
                endts = event[3][:10]+"T09:00:00Z"
                extra = max(0.0,calculate_time(endts,event[3]).total_seconds()/3600.0)
                hours = 4.0 + extra
        print(str(hours)+" hours")
        events[i].append(hours)
    return events
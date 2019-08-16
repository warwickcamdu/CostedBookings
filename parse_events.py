from collect_events import collect_events

def parse_events(events):

    """
    Makes the mess that google calendar returns into something workable

    Filters through all received events from gcal and only returns those we are
    interested in. Also, calculates how long each event is and appends that
    to each event.

    Parameters
    ----------
    events : list
        List of events retrieved from the relevant calendars
    
    Returns
    -------
    all_events: list of lists
        Filtered, parsed events in a matrix-like structure

    
    """


    all_events = []
    for cal in events:
        for event in cal['items']:
            if ('displayName' in event['organizer'] and 'summary' in event and 'dateTime' in event['start'] and 'dateTime' in event['end']):
                timedelta = calculate_time(event['start']['dateTime'],event['end']['dateTime'])
                all_events.append([event['organizer']['displayName'],event['summary'],event['start']['dateTime'],event['end']['dateTime'],timedelta.total_seconds()/3600.0])
    return all_events

def get_first_names(events):

    """
    Parses first name of bookers from the events

    From the raw gcal data, create a similar output from the previous function,
    but with a field that is first name of booker + email.

    Parameters
    ----------
    events : list
        List of events retrieved from the relevant calendars
    
    Returns
    -------
    all_events: list of lists
        Filtered, parsed events in a matrix-like structure

    
    """
    
    all_events = []
    for cal in events:
        for event in cal['items']:
            if ('displayName' in event['organizer'] and 'summary' in event and 'dateTime' in event['start'] and 'dateTime' in event['end']):
                timedelta = calculate_time(event['start']['dateTime'],event['end']['dateTime'])
                booker = event['summary'].replace("/"," ").replace("-"," ").replace(","," ").replace("+"," ").split()[0].title()
                if 'email' in event['creator']:
                    booker = booker + " " + event['creator']['email']
                all_events.append([event['organizer']['displayName'],booker,event['start']['dateTime'],event['end']['dateTime'],timedelta.total_seconds()/3600.0])
    return all_events


def calculate_time(start,end):

    """
    Calculates a time delta between start and end.

    
    """

    from datetime import datetime
    FMT = ["%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S+01:00"]
    tdelta = 0
    
    
    for form in FMT:
        try:
            startdt = datetime.strptime(start, form)
            
        except ValueError:
            pass
    for form in FMT:
        try:
            enddt = datetime.strptime(end, form)
            
        except ValueError:
            pass
    tdelta = enddt - startdt
    return tdelta


if __name__ == "__main__":
    events = collect_events("legacy/allevents.txt")
    allevents = parse_events(events)
    print(allevents)


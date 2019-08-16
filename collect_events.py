from generate_date import generate_date, increase_month, generate_last_year, generate_this_year
from retrieve_calendars import retrieve_calendars
from retrieve_events import retrieve_events
from create_service import create_service

def collect_events(filename):
    """
    Sets date limits and retrieves events in the range.

    Creates date objects for the beginning and the end of the period 
    (in this case, the month before the current one), a Google service, 
    retrieves the calendars and then the events in the desired range of dates.

    Parameters
    ----------
    filename : str
        filepath where the events will be saved.
    
    Returns
    -------
    events: list
        List of events retrieved from the relevant calendars

    """
    date_begin = generate_date()
    date_end = increase_month(date_begin)
    service = create_service()
    calendars = retrieve_calendars(service)
    

    events = retrieve_events(service, calendars, date_begin, date_end)
    #print(events)
    #events = [x.encode('utf-8') for x in events]
    f = open(filename, "w")

    print(events, file=f)
    return events


def collect_events_allyear(filename):
    """
    Sets date limits and retrieves events in the range.

    Creates date objects for the beginning and the end of the period 
    (in this case, the whole of last year), a Google service, 
    retrieves the calendars and then the events in the desired range of dates.

    Parameters
    ----------
    filename : str
        filepath where the events will be saved.
    
    Returns
    -------
    events: list
        List of events retrieved from the relevant calendars

    """
    date_begin = generate_last_year()
    date_temp = generate_date()
    date_end = increase_month(date_temp)
    
    service = create_service()
    calendars = retrieve_calendars(service)
    

    events = retrieve_events(service, calendars, date_begin, date_end)
    #print(events)
    #for x in events: print(x)
    #events = [x.encode('utf-8') for x in events]
    f = open(filename, "w")

    print(events, file=f)
    return events


def collect_events_thisyear(filename):
    """
    Sets date limits and retrieves events in the range.

    Creates date objects for the beginning and the end of the period 
    (in this case, the whole of this year), a Google service, 
    retrieves the calendars and then the events in the desired range of dates.

    Parameters
    ----------
    filename : str
        filepath where the events will be saved.
    
    Returns
    -------
    events: list
        List of events retrieved from the relevant calendars

    """
    date_begin = generate_this_year()
    date_temp = generate_date()
    date_end = increase_month(date_temp)
    service = create_service()
    calendars = retrieve_calendars(service)
    

    events = retrieve_events(service, calendars, date_begin, date_end)
    #print(events)
    #for x in events: print(x)
    #events = [x.encode('utf-8') for x in events]
    f = open(filename, "w")

    print(events, file=f)
    return events


if __name__ == "__main__":
    events = collect_events("legacy/allevents.txt")

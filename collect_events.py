from generate_date import generate_date, increase_month
from retrieve_calendars import retrieve_calendars
from retrieve_events import retrieve_events
from create_service import create_service

def collect_events():
    date_begin = generate_date()
    date_end = increase_month(date_begin)
    service = create_service()
    calendars = retrieve_calendars(service)
    

    events = retrieve_events(service, calendars, date_begin, date_end)
    return events



if __name__ == "__main__":
    events = collect_events()

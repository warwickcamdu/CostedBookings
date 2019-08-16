def retrieve_events(service, calendars, date_begin, date_end):
    """
    Loops over calendars and returns all events in those, given a date range

    Uses the created service to retrieve all events from a list of calendars
    inside a given date range.

    Parameters
    ----------
    service :
        A Resource object with methods for interacting with the Google service.
    
    Returns
    -------
    events_result: list
        List of events retrieved from the all calendars

    """
    events_result = []
    for id in calendars:
        events_result.append(service.events().list(calendarId=id, timeMin=date_begin,
                                                   timeMax=date_end, singleEvents=True,
                                                   orderBy='startTime').execute())

    return events_result


if __name__ == "__main__":
    from create_service import create_service
    from retrieve_calendars import retrieve_calendars
    service = create_service()
    calendars = retrieve_calendars(service)
    res = retrieve_events(service, calendars, "2019-07-10T00:00:00.00000Z", "2019-07-13T00:00:00.00000Z")
    print(res)

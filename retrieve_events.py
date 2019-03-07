def retrieve_events(service, calendars, date_begin, date_end):
    events_result = []
    for id in calendars:
        events_result.append(service.events().list(calendarId=id, timeMin=date_begin,
                                        timeMax=date_end, maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute())
    
    return events_result
def retrieve_events(service, calendars, date):

    for id in calendars:
        events_result = service.events().list(calendarId=id, timeMin=date,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    
    return events_result
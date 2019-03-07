from collect_events import collect_events

def parse_events(events):
    all_events = []
    for cal in events:
        for event in cal['items']:
            if ('displayName' in event['organizer'] and 'summary' in event and 'dateTime' in event['start'] and 'dateTime' in event['end']):
                all_events.append([event['organizer']['displayName'],event['summary'],event['start']['dateTime'],event['end']['dateTime']])
    return all_events


if __name__ == "__main__":
    events = collect_events()
    allevents = parse_events(events)
    print(allevents)
from collect_events import collect_events

def parse_events(events):
    all_events = []
    for cal in events:
        print(cal['summary'])
        for event in cal['items']:
            all_events.append(event['summary'])
    return all_events


if __name__ == "__main__":
    events = collect_events()
    allevents = parse_events(events)
    print(allevents)
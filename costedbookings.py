from collect_events import collect_events
from parse_events import parse_events
from write_output import write_output

def costedbookings():
    filename_all = "legacy/allevents.txt"
    events = collect_events(filename_all)
    parsed_events = parse_events(events)
    filename = "legacy/test.csv"
    write_output(parsed_events,filename)


if __name__ == "__main__":
    costedbookings()
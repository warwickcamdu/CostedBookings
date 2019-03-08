from collect_events import collect_events
from parse_events import parse_events, get_first_names
from write_output import write_output, write_hours
from consolidate_hours import consolidate_hours
from cost_hours import cost_hours

def costedbookings():
    filename_all = "legacy/allevents.txt"
    events = collect_events(filename_all)

    parsed_events = parse_events(events)

    filename = "legacy/events_full_name.csv"
    write_output(parsed_events,filename)

    parseagain = get_first_names(events)

    parsecost = cost_hours(parseagain)

    filename = "legacy/events_first_name.csv"
    write_output(parsecost,filename)
    
    frame = consolidate_hours(parseagain)

    filename = "legacy/total_hours.csv"
    frame.to_csv(filename)

if __name__ == "__main__":
    costedbookings()
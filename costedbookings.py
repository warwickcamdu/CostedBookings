from collect_events import collect_events
from parse_events import parse_events, get_first_names
from write_output import write_output, write_hours
from consolidate_hours import consolidate_hours, add_costcodes
from cost_hours import cost_hours
from generate_costs import generate_costs

def costedbookings():
    """
    Main function - sets everything else into motion.

    Collects, parses (in multiple ways) and analyses the calendar
    events. Writes outputs. This version uses all events from the
    previous calendar month.

    
    """
    filename_all = "legacy/allevents.txt"
    events = collect_events(filename_all)

    parsed_events = parse_events(events)

    filename = "legacy/events_first_name.csv"
    write_output(parsed_events,filename)

    parseagain = get_first_names(events)

    parsecost = cost_hours(parseagain)
    parsecost = add_costcodes(parsecost)

    filename = "legacy/events_full_name.csv"
    write_output(parsecost,filename)
    frame = consolidate_hours(parseagain)
    
    filename = "legacy/total_hours.csv"
    frame.to_csv(filename)

    frame = generate_costs(frame)
    filename = "legacy/costed_bookings.csv"
    frame.to_csv(filename,float_format='%.2f')

if __name__ == "__main__":
    costedbookings()
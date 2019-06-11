from collect_events import collect_events, collect_events_allyear, collect_events_thisyear
from parse_events import parse_events, get_first_names
from write_output import write_output, write_hours
from consolidate_hours import consolidate_hours, add_costcodes
from cost_hours import cost_hours
from generate_costs import generate_costs

def costedbookings():
    filename_all = "legacy/thisyear_allevents.txt"
    events = collect_events_thisyear(filename_all)

    parsed_events = parse_events(events)

    filename = "legacy/thisyear_events_first_name.csv"
    write_output(parsed_events,filename)

    parseagain = get_first_names(events)

    parsecost = cost_hours(parseagain)
    parsecost = add_costcodes(parsecost)

    filename = "legacy/thisyear_events_full_name.csv"
    write_output(parsecost,filename)
    frame = consolidate_hours(parseagain)
    
    filename = "legacy/thisyear_total_hours.csv"
    frame.to_csv(filename)

    frame = generate_costs(frame)
    filename = "legacy/thisyear_costed_bookings.csv"
    frame.to_csv(filename,float_format='%.2f')

if __name__ == "__main__":
    costedbookings()
def write_output(events, filename):
    import csv
    f = open(filename, "w")

    f.write("Calendar, Booking, Start, End\n")
    writer = csv.writer(f)
    writer.writerows(events)



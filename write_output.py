def write_output(events, filename):

    """
    Writes a list of lists to a file (with a header).

    
    """

    import csv
    f = open(filename, "w")

    f.write("Calendar,Booking,Start,End,Duration(h),Cost Hours(h),day of the week,Cost code\n")
    writer = csv.writer(f)
    writer.writerows(events)

def write_hours(hours, micros, filename):

    """
    Not being used.

    
    """

    import csv
    f = open(filename, "w")

    f.write("User")
    for micro in micros:
        f.write(","+micro)
    f.write("\n")
    writer = csv.writer(f)
    writer.writerows(hours)



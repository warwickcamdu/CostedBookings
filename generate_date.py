def generate_date(current=None):
    """
    Generates a date that is the 1st of the previous calendar month.
    The only trickery here is dealing with timezones/daylight savings

    
    """
    import datetime
    from strict_rfc3339 import validate_rfc3339
    if (not current):
        now = datetime.datetime.now().isoformat('T')+"Z"
    else:
        if validate_rfc3339(current):
            now=current
        else:
            return None
    month = int(now[5:7])
    month = month - 1
    beg_month = now[0:5]+"%02d"%month+"-01T00:00:00.00000Z"
    return beg_month


def generate_last_year(current=None):
    """
    Generates a date that is the 1st day of the previous calendar yeah.
    The only trickery here is dealing with timezones/daylight savings

    
    """
    import datetime
    from strict_rfc3339 import validate_rfc3339
    if (not current):
        now = datetime.datetime.now().isoformat('T')+"Z"
    else:
        if validate_rfc3339(current):
            now=current
        else:
            return None
    month = int(now[5:7])
    year = int(now[0:4])
    year = year - 1
    beg_month = "%04d"%year+"-"+"%02d"%month+"-01T00:00:00.00000Z"
    return beg_month

def generate_this_year(current=None):

    """
    Generates a date that is the 1st day of the current calendar month.
    The only trickery here is dealing with timezones/daylight savings

    
    """

    import datetime
    from strict_rfc3339 import validate_rfc3339
    if (not current):
        now = datetime.datetime.now().isoformat('T')+"Z"
    else:
        if validate_rfc3339(current):
            now=current
        else:
            return None
    year = int(now[0:4])
    #year = year - 1
    beg_month = "%04d"%year+"-"+"01"+"-01T00:00:00.00000Z"
    return beg_month


def increase_month(date):

    """
    Increases a month on the received date. Needs to account
    for changing years if December

    
    """

    from strict_rfc3339 import validate_rfc3339
    if not validate_rfc3339(date):
        return None
    month = int(date[5:7])
    month = month + 1
    if (month == 13):
        month = 1
        year = int(date[0:4])
        year = year + 1
        date = "%04d"%year+date[4:]
    newdate = date[0:5]+"%02d"%month+"-01T00:00:00.00000Z"
    return newdate


if __name__ == "__main__":
    print(generate_last_year())
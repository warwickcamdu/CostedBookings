def generate_date(current=None):
    import datetime
    import pytz
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


if __name__ == "__main__":
    print(generate_date())
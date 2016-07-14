from datetime import date, datetime, timedelta

from datetime import timedelta


def week_range(date):
    """Find the first/last day of the week for the given day.
    Assuming weeks start on Sunday and end on Saturday.

    Returns a tuple of ``(start_date, end_date)``.

    """
    # isocalendar calculates the year, week of the year, and day of the week.
    # dow is Mon = 1, Sat = 6, Sun = 7
    year, week, dow = date.isocalendar()

    # Find the first day of the week.
    if dow == 7:
        # Since we want to start with Sunday, let's test for that condition.
        start_date = date
    else:
        # Otherwise, subtract `dow` number days to get the first day
        start_date = date - timedelta(dow)

    # Now, add 6 for the last day of the week (i.e., count up to Saturday)
    end_date = start_date + timedelta(6)

    return (start_date, end_date)


def datespan(startDate, endDate, delta=timedelta(days=7)):
    currentDate = startDate
    while currentDate < endDate:
        yield currentDate
        currentDate += delta


# for day in datespan(date(2007, 3, 30), date(2007, 5, 3),
#     delta=timedelta(days=7)):
#     print day

# get week range based on date
d = datetime(2013, 3, 7)
print week_range(d)

# based on ist calender
def foo(year, week):
    d = date(year,1,1)
    d = d - timedelta(d.weekday())
    dlt = timedelta(days = (week-1)*7)
    return d + dlt,  d + dlt + timedelta(days=6)

print foo(2016, 3)
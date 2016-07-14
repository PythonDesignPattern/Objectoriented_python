import datetime


def first_day_of_month():
    week_number = '1'
    d = "2016-W"+week_number
    date_format = '%Y-%m-%d'
    day_interval = 8
    start_date = datetime.datetime.strptime(d + '-0', "%Y-W%W-%w",).strftime(date_format)
    date_object = datetime.datetime.strptime(start_date, date_format)
    end_date = (date_object + datetime.timedelta(days=day_interval)).strftime(date_format)

    print start_date
    print end_date
    # The - 0 and - % w pattern tells the parser to pick the sunday in that week.

first_day_of_month()

# import datetime
# today = datetime.date(2014, 9, 30)
# next_week = today + datetime.timedelta(days=7)
# next_week.isocalendar()[1]
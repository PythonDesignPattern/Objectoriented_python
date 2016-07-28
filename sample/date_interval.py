from datetime import datetime, timedelta
from collections import OrderedDict

dates = ["1900-01", "3000-12"]


def monthlist_fast(dates):
    start, end = [datetime.strptime(_, "%Y-%m") for _ in dates]
    total_months = lambda dt: dt.month + 12 * dt.year
    print total_months(end)-(total_months(start)-1)
    # mlist = []
    # for tot_m in xrange(total_months(start)-1, total_months(end)):
    #     y, m = divmod(tot_m, 12)
    #     mlist.append(datetime(y, m+1, 1).strftime("%b-%y"))
    # print len(mlist)
    # return mlist

monthlist_fast(dates)

from datetime import datetime, timedelta
from collections import OrderedDict

dates = ["1900-1-1", "2050-12-31"]

def monthlist_short(dates):
    start, end = [datetime.strptime(_, "%Y-%m-%d") for _ in dates]
    return OrderedDict(((start + timedelta(_)).strftime(r"%b-%y"), None) for _ in xrange((end - start).days)).keys()

def monthlist_fast(dates):
    start, end = [datetime.strptime(_, "%Y-%m-%d") for _ in dates]
    total_months = lambda dt: dt.month + 12 * dt.year

    mlist = []
    for tot_m in range(total_months(start)-1, total_months(end)):
        y, m = divmod(tot_m, 12)
        mlist.append(datetime(y, m+1, 1).strftime("%b-%y"))
    return mlist

# assert monthlist_fast(dates) == monthlist_short(dates)

if __name__ == "__main__":
    from timeit import Timer
    for func in "monthlist_short", "monthlist_fast":
        print func, Timer("%s(dates)" % func, "from __main__ import dates, %s" % func).timeit(1000)
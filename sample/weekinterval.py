import datetime

start_year = 2016
start_week = 12
end_year = 2016
end_week = 23

year_diff = end_year-start_year
# print "Week Range"
# for week
# for year in range(start_year, end_year+1):
#     print "Curent year "+str(year)
#     if start_year == end_year:
#         for week in range(start_week, end_week+1):
#             print str(year)+"--"+str(week)
#     elif year == start_year:
#         for week in range(start_week, (int(datetime.date(year, 12, 28).isocalendar()[1]))+1):
#             print str(start_year) + "--" + str(week)
#     elif year == end_year and start_year != end_year:
#         for week in range(1, end_week + 1):
#             print str(end_year) + "--" + str(week)
#     else:
#         for week in range(1, int(datetime.date(year, 12, 28).isocalendar()[1])):
#             print str(year)+"--"+str(week)

print "Month Range"
# for month
start_year = 2015
start_month = 3
end_year = 2016
end_month = 10
for year in range(start_year, end_year+1):
    print "current year "+str(year)
    if start_year == end_year:
        for month in range(start_month, end_month + 1):
            print str(year) + "--" + str(month)
    elif year == start_year:
        for month in range(start_month, 13):
            print str(start_year) + "--" + str(month)
    elif year == end_year and start_year != end_year:
        for month in range(1, end_month + 1):
            print str(end_year) + "--" + str(month)
    else:
        for month in range(1, 13):
            print str(year)+"--"+str(month)

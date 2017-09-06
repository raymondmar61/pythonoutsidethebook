#Get Last Day of the Month
#https://stackoverflow.com/questions/42950/get-last-day-of-the-month-in-python

import calendar
#Mon is 0, Tue is 1, Sat is 5, Sun is 6
print(calendar.monthrange(2002,1)) #print (1, 31) or Tue is first day Jan has 31 days
print(calendar.monthrange(2002,1)[1]) #print 31 Jan has 31 days
print(calendar.monthrange(2002,1)[0]) #print 1 Tue is first day Jan
print(calendar.monthrange(2008,2)) #print (4, 31) or Fri is first day Feb has 29 days

import datetime
def lastdayofmonth(anyday):
	nextmonth = anyday.replace(day=28) + datetime.timedelta(days=4)
	#print("nextmonth",nextmonth)
	#print("datetime timedelta",datetime.timedelta(days=nextmonth.day))
	return nextmonth - datetime.timedelta(days=nextmonth.day)
for month in range(1,13):
	print(lastdayofmonth(datetime.date(2012, month, 1))) #print 2012-01-31\n 2012-02-29\n 2012-03-31\n 2012-04-30\n 2012-05-31\n 2012-06-30\n 2012-07-31\n 2012-08-31\n 2012-09-30\n 2012-10-31\n 2012-11-30\n 2012-12-31
print("\n")

date = datetime.datetime.now()
print("today is",date)
print("the first day of the present month is",date.replace(day=1))
print("the last day of the present month is",date.replace(day=calendar.monthrange(date.year, date.month)[1]))
print("\n")

now = datetime.datetime.now()
startmonth = datetime.datetime(now.year, now.month, 1)
print("startmonth",startmonth) #print 2017-09-01 00:00:00
dateonnextmonth = startmonth + datetime.timedelta(35) #days= is timedelta default?
print(dateonnextmonth) #print 2017-10-06 00:00:00
startnextmonth = datetime.datetime(dateonnextmonth.year, dateonnextmonth.month,1)
print(startnextmonth) #print 2017-10-01 00:00:00
lastdaymonth = startnextmonth - datetime.timedelta(days=1) #days= is timedelta default?
print(lastdaymonth) #2017-09-30 00:00:00
print("\n")

#selecteddate = date(someyear, somemonth, someday)
selecteddate = datetime.date(2012, 7, 5)
if selecteddate.month == 12:
	lastdayselectedmonth = datetime.date(selecteddate.year, selecteddate.month, 31)
else:
	lastdayselectedmonth = datetime.date(selecteddate.year, selecteddate.month +1, 1) - datetime.timedelta(days=1)
print(lastdayselectedmonth) #print 2012-07-31
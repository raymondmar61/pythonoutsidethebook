import datetime

firstdate = datetime.date(2017, 1, 30)
print(firstdate) #print 2017-01-30
print(firstdate.strftime("%A %B %d, %Y")) #print Monday January 30, 2017
secondate = datetime.date(2017, 2, 1)
print(secondate) #print 2017-02-01
print(secondate.strftime("%A %B %d, %Y")) #print Wednesday February 01, 2017
print(secondate - firstdate) #print 2 days, 0:00:00
print((secondate - firstdate).days) #print 2

now = datetime.datetime.today()
print(now) #print 2017-11-30 18:09:38.741071
print(type(now)) #print <class 'datetime.datetime'>
print(now.strftime("%Y-%m-%d")) #print 2017-11-30
c = now.strftime("%Y-%m-%d")
print(c) #print 2017-11-30
print(type(c)) #print <class 'str'>

a = datetime.date(2011,11,24)
b = datetime.date(2011,11,17)
print(a-b) #print 7 days, 0:00:00
print((a-b).days) #print 7

now = datetime.datetime.today()
comparedate = datetime.datetime.strptime("11/24/2017","%m/%d/%Y")
print(now) #print 2017-11-30 18:12:51.894033
print(comparedate) #print 2017-11-24 00:00:00
print(type(now)) #print <class 'datetime.datetime'>
print(type(comparedate)) #print <class 'datetime.datetime'>
print((now-comparedate).days) #print 6

month = 5
day = 17
year = 2007
c = datetime.date(year, month, day)
print(c) #print 2007-05-17
print(type(c)) #print <class 'datetime.date'>
c = str(c)
print(datetime.datetime.strptime(c,"%Y-%m-%d")) #print 2007-05-17 00:00:00
print(type(c)) #print <class 'str'>
cstring = (datetime.datetime.strptime(c,"%Y-%m-%d"))
print(type(cstring)) #print <class 'datetime.datetime'>
now = datetime.datetime.today()
print(now) #print 2017-11-30 18:12:51.894033
print(type(now)) #print <class 'datetime.datetime'>
print((now-cstring).days) #print 3850

#from codecademy #2 Strings & Console Output
from datetime import datetime
print(datetime.now()) #print current datetime such as 2017-07-21 18:35:41.046993
print(datetime.now().year) #print 2017
print(datetime.now().month) #print 7
print(datetime.now().day) #print 21
now = datetime.now()
print(now) #print 2017-07-21 18:42:19.619062
print(now.year) #print 2017
print(now.month) #print 7
print(now.day) #print 21
print("%s/%s/%s" % (now.month, now.day, now.year)) #print 7/24/2017
print("%s:%s:%s" % (now.hour, now.minute, now.second)) #print 11:59:39
print("%s/%s/%s %s:%s:%s" % (now.month, now.day, now.year, now.hour, now.minute, now.second)) #print 7/24/2017 12:1:49

#https://stackoverflow.com/questions/31955761/converting-python-string-to-datetime-obj-with-am-pm
#datetime.strptime() is used for converting a string to a datetime object , when using strptime() you have to specify the correct format in which the date/time in the string exists.
test = "05/16/18"
print(datetime.strptime(test, "%m/%d/%y")) #print 2018-05-16 00:00:00
test2 = "05/16/2018"
print(datetime.strptime(test2, "%m/%d/%Y")) #print 2018-05-16 00:00:00
test = "2015-08-12 13:07:32"
print(datetime.strptime(test, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %I:%M:%S %p')) #print 2015-08-12 01:07:32 PM
#https://stackoverflow.com/questions/13855111/how-can-i-convert-24-hour-time-to-12-hour-time
timetodayam = datetime.strptime("10:30", "%H:%M").strftime("%I:%M %p")
print(timetodayam) #print 10:30 AM
timetodaypm = datetime.strptime("22:30", "%H:%M").strftime("%I:%M %p")
print(timetodaypm) #print 10:30 PM
print(timetodaypm.lower()) #print 10:30 pm

#https://stackoverflow.com/questions/12033905/using-python-to-create-an-average-out-of-a-list-of-times
#You don't want to average times on hours, minutes, and seconds.  Convert all times into seconds, calculate the average, and convert back to hours, minutes, and seconds.
from datetime import timedelta

def averagetime(timelist):
	timeinseconds = []
	for eachtimelist in timelist:
		h, m, s = map(int, eachtimelist.split(":"))
		timeinseconds.append((h*3600)+(m*60)+s)
	#print(timeinseconds)
	#print(sum(timeinseconds)/len(timeinseconds))
	averagetime = sum(timeinseconds)/len(timeinseconds)
	#days = divmod(averagetime, 86400) # Get days (without [0]!)
	#hours = divmod(days[1], 3600) # Use remainder of days to calc hours
	hours = divmod(averagetime, 3600) # Use remainder of seconds to calc hours
	minutes = divmod(hours[1], 60) # Use remainder of hours to calc minutes
	seconds = divmod(minutes[1], 1) # Use remainder of minutes to calc seconds
	return ("Average time is {} hours, {} minutes, and {} seconds".format(int(hours[0]), int(minutes[0]), seconds[0]))	
print(averagetime(["00:59:00","1:1:00"])) #print Average time is 1 hours, 0 minutes, and 0.0 seconds
print(averagetime(["00:59:00","1:1:00","1:23:54"])) #print Average time is 1 hours, 7 minutes, and 58.0 seconds
#RM:  Calculating time difference greater than 24 hours inspired from statisticsforanathleticassociation.py.   There is no bullshit : pipes.
from datetime import timedelta, datetime
times = ["1:15:59", "1:47:06", "1:17:20", "1:32:34", "2:3:17", "30:15:59", "48:2:41"]

#https://stackoverflow.com/questions/2922735/python-time-objects-with-more-than-24-hours
firsttime = timedelta(hours=36)
secondtime = timedelta(hours=4, minutes=46, seconds=23)
timedifference = secondtime - firsttime
print(timedifference) #print -2 days, 16:46:23

#https://stackoverflow.com/questions/34134971/python-format-timedelta-greater-than-24-hours-for-display-only-containing-hours
impropertimes = ["1:15:59", "1:47:06", "1:17:20", "1:32:34", "2:3:17", "30:15:59", "48:2:41"]
propertime = []
for x in impropertimes:
	x = x.split(":")
	xinteger = []
	for convertxtointeger in x:
		xinteger.append(int(convertxtointeger))
	realtime = timedelta(hours=xinteger[0], minutes=xinteger[1], seconds=xinteger[2])
	print(realtime)
	'''
	1:15:59
	1:47:06
	1:17:20
	1:32:34
	2:03:17
	1 day, 6:15:59
	2 days, 0:02:41
	'''
	propertime.append(realtime)
print(propertime) #print [datetime.timedelta(0, 4559), datetime.timedelta(0, 6426), datetime.timedelta(0, 4640), datetime.timedelta(0, 5554), datetime.timedelta(0, 7397), datetime.timedelta(1, 22559), datetime.timedelta(2, 161)]

#https://stackoverflow.com/questions/18303301/working-with-time-values-greater-than-24-hours.  These are not times but durations, and the representation of a duration is a timedelta.  RM:  code doesn't work.  Fact is good.

#https://stackoverflow.com/questions/1345827/how-do-i-find-the-time-difference-between-two-datetime-objects-in-python
earlierdate = datetime(2019, 3, 23, 21, 8, 15)
laterdate = datetime(2019, 5, 30, 17, 9, 45)
timedifference = earlierdate - laterdate
print(timedifference) #print -86 days, 3:58:30
print(timedifference.total_seconds()) #print -7416090.0
timedifferenceinseconds = timedifference.total_seconds()
print("Number of days",divmod(timedifferenceinseconds,86400)[0]) #print Number of days -68.0.  86400 seconds in a day
print("Number of hours",divmod(timedifferenceinseconds,3600)[0]) #print Number of hours -1629.0.  3600 seconds in an hour
print("Number of minutes",divmod(timedifferenceinseconds,60)[0]) #print Number of minutes -97682.0.  60 seconds in an hour
print("Number of seconds",timedifferenceinseconds) #print Number of seconds -5860890.0
days = divmod(timedifferenceinseconds, 86400) # Get days (without [0]!)
print(days) #print (-68.0, 14310.0)
hours = divmod(days[1], 3600) # Use remainder of days to calc hours
print(hours) #print (3.0, 3510.0)
minutes = divmod(hours[1], 60) # Use remainder of hours to calc minutes
print(minutes) #print (58.0, 30.0)
seconds = divmod(minutes[1], 1) # Use remainder of minutes to calc seconds
print(seconds) #print (30.0, 0.0)
print("Time between earlierdate and laterdate {} days, {} hours, {} minutes, and {} seconds".format(days[0], int(hours[0]), int(minutes[0]), seconds[0])) #print Time between earlierdate and laterdate -68.0 days, 3 hours, 58 minutes, and 30.0 seconds

#https://stackoverflow.com/questions/34134971/python-format-timedelta-greater-than-24-hours-for-display-only-containing-hours
propertime = []
for x in times:
	x = x.split(":")
	xinteger = []
	for convertxtointeger in x:
		xinteger.append(int(convertxtointeger))
	realtime = timedelta(hours=xinteger[0], minutes=xinteger[1], seconds=xinteger[2])
	print("Real time",realtime)
	seconds = realtime.total_seconds()
	hours = seconds // 3600
	minutes = (seconds % 3600) // 60
	seconds = seconds % 60
	print("Formatted time {}:{:02d}:{:02d}".format(int(hours),int(minutes),int(seconds)))
'''
Real time 1:15:59
Formatted time 01:15:59
Real time 1:47:06
Formatted time 01:47:06
Real time 1:17:20
Formatted time 01:17:20
Real time 1:32:34
Formatted time 01:32:34
Real time 2:03:17
Formatted time 02:03:17
Real time 1 day, 6:15:59
Formatted time 30:15:59
Real time 2 days, 0:02:41
Formatted time 48:02:41
'''

#two times greater than 24 hours
firsttime = "25:40:5"
secondtime = "30:10:7"
firsttimesplit = firsttime.split(":")
print(firsttimesplit)
secondtimesplit = secondtime.split(":")
print(secondtimesplit)
firsttimeproper = timedelta(hours=int(firsttimesplit[0]), minutes=int(firsttimesplit[1]), seconds=int(firsttimesplit[2]))
secondtimeproper = timedelta(hours=int(secondtimesplit[0]), minutes=int(secondtimesplit[1]), seconds=int(secondtimesplit[2]))
timedifference = secondtimeproper - firsttimeproper
print(timedifference) #print 4:30:02

#https://stackoverflow.com/questions/2780897/python-summing-up-time
timelist = ["0:00:00","0:00:15","9:30:56"]
sumtime = timedelta(hours=0, minutes=0, seconds=0)
for eachtimelist in timelist:
	splittime = [int(eachtimelistsplit) for eachtimelistsplit in eachtimelist.split(":")]
	timeproper = timedelta(hours=int(splittime[0]), minutes=int(splittime[1]), seconds=int(splittime[2]))
	print(timeproper)
	'''
	0:00:00
	0:00:15
	9:30:56
	'''
	sumtime += timeproper
print(sumtime) #print 9:31:11

timelist = ["0:00:00","0:00:15","9:30:56"]
sumtime = timedelta()
for eachtimelist in timelist:
	(h, m, s) = eachtimelist.split(":")
	print(h, m, s)
	'''
	0 00 00
	0 00 15
	9 30 56
	'''
	timeproper = timedelta(hours=int(h), minutes=int(m), seconds=int(s))
	sumtime += timeproper
print(sumtime) #print 9:31:11

timelist = ["0:00:00","0:00:15","9:30:56"]
sumtime = 0
for eachtimelist in timelist:
	h, m, s = map(int, eachtimelist.split(":"))
	print(h, m, s)
	'''
	0 0 0
	0 0 15
	9 30 56
	'''
	sumtime += 3600*h + 60*m + s
print("%02d:%02d:%02d"%(sumtime/3600, sumtime/60 % 60, sumtime %60)) #print 09:31:11

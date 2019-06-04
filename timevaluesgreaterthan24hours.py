#RM:  Calculating time difference greater than 24 hours inspired from statisticsforanathleticassociation.py.   There is no bullshit : pipes.
from datetime import timedelta, datetime
times = ["1:15:59", "1:47:06", "1:17:20", "1:32:34", "2:3:17", "30:15:59", "48:2:41"]

#https://stackoverflow.com/questions/2922735/python-time-objects-with-more-than-24-hours
firsttime = timedelta(hours=36)
secondtime = timedelta(hours=4, minutes=46, seconds=23)
timedifference = secondtime - firsttime
print(timedifference) #print -2 days, 16:46:23

#https://stackoverflow.com/questions/18303301/working-with-time-values-greater-than-24-hours.  These are not times but durations, and the representation of a duration is a timedelta.  RM:  code doesn't work.  Fact is good.

#https://stackoverflow.com/questions/34134971/python-format-timedelta-greater-than-24-hours-for-display-only-containing-hours
propertime = []
for x in times:
	x = x.split(":")
	xinteger = []
	for convertxtointeger in x:
		xinteger.append(int(convertxtointeger))
	realtime = timedelta(hours=xinteger[0], minutes=xinteger[1], seconds=xinteger[2])
	print(realtime)
	propertime.append(realtime)
print(propertime) #print [datetime.timedelta(0, 4559), datetime.timedelta(0, 6426), datetime.timedelta(0, 4640), datetime.timedelta(0, 5554), datetime.timedelta(0, 7397), datetime.timedelta(1, 22559), datetime.timedelta(2, 161)]

#https://stackoverflow.com/questions/34134971/python-format-timedelta-greater-than-24-hours-for-display-only-containing-hours
propertime = []
for x in times:
	x = x.split(":")
	xinteger = []
	for convertxtointeger in x:
		xinteger.append(int(convertxtointeger))
	realtime = timedelta(hours=xinteger[0], minutes=xinteger[1], seconds=xinteger[2])
	print(realtime)
	seconds = realtime.total_seconds()
	hours = seconds // 3600
	minutes = (seconds % 3600) // 60
	seconds = seconds % 60
	print("Formatted time {}:{}:{}".format(int(hours),int(minutes),int(seconds)))
'''
1:15:59
Formatted time 1:15:59
1:47:06
Formatted time 1:47:6
1:17:20
Formatted time 1:17:20
1:32:34
Formatted time 1:32:34
2:03:17
Formatted time 2:3:17
1 day, 6:15:59
Formatted time 30:15:59
2 days, 0:02:41
Formatted time 48:2:41
'''
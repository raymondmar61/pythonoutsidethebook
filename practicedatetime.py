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

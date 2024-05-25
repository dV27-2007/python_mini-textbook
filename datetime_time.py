# DATETIME
# datetime module amsatveri jameri het ashxatelu hamar e
import datetime

print(dir(datetime))# moduli bolor hatkanishnere paronakox cucak
#['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__',
# '__doc__', '__file__', '__loader__', '__name__',
#'__package__', '__spec__', '_divide_and_round', 'date', 'datetime',
# 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']

#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
# Datetime moduli aravel hachax ogtagorcvox daseren en(datetime.datetime, datetime.date, datetime.time, datetime.timedelta)
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------

# datetime.datetime - nerkayacnum e jamanaki mek ket, amsative yev jame

# talis e chshgrit datan yev jamanake
now = datetime.datetime.now()
print(now)# (year-month-day hour:minute:second.microsecond)

#---------------------------------------------------

# datetime.datetime(year, month, day)
a = datetime.datetime(2024, 5, 25)
print(a)# 2024-05-25 00:00:00

# datetime.datetime(year, month, day, hour, minute, second, microsecond)
b = datetime.datetime(2022, 12, 28, 23, 55, 59, 342380)
print(b)# 2022-12-28 23:55:59.342380

#---------------------------------------------------


a = datetime.datetime(2024, 5, 25, 23, 55, 59, 342380)

print("Year =", a.year)# tarin = 2024
print("Month =", a.month)# amise = 05
print("Day =", a.day)# ore = 25
print("Hour =", a.hour)# jame = 23
print("Minute =", a.minute)# ropen = 55
print("Second =", a.second)# varkyane = 59
print("Microsecond =", a.microsecond)# milivarkyane = 342380
print("Timestamp =", a.timestamp())# jamanaki droshume = 1511913359.34238

#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
# datetime.date - nerkayacnum e amsative (year, month, day) aranc jamanaki

# talis e miayn chshgrit datan
date_today = datetime.date.today()
print(date_today)# (year-month-day)

#---------------------------------------------------

# date() talis e 'date classe'-i konstrukter
d = datetime.date(2024, 5, 25)
print(d)# (2024-05-25)

#karelie nayev ayspses

from datetime import date
d1 = date(2023,5,25)
print(d1)# (2024-05-25)

#---------------------------------------------------

print(datetime.date.today())# talis e aysorva amsative (year-month-day)

#---------------------------------------------------

# menq karox enq jamanaki droshume veracnel amsatvi ays metodov
timestamp = datetime.date.fromtimestamp(1326244364)
print(timestamp)# (2012-01-11)

#---------------------------------------------------

today = datetime.date.today()# talis e ays orva amsative

print("Current year:", today.year)# himikva tarin
print("Current month:", today.month)# himikva amise
print("Current day:", today.day)# himikva ore


#----------------------------------------------------------------------
#----------------------------------------------------------------------
#----------------------------------------------------------------------
# datetime.time - nerkayacnum e jamanke (hour,minute,second,microsecond)

from datetime import time

# datetime.time(hour = 0, minute = 0, second = 0)
a = time()
print(a)# 00:00:00

# time(hour, minute, second, microsecond)
b = datetime.time(11, 34, 56, 234566)
print(b)# 11:34:56.234566

c = datetime.time(hour=11, minute=34, second=56, microsecond=234566)
print(c)# 11:34:56.234566

#---------------------------------------------------

a = time(11, 34, 56)

print("Hour =", a.hour)# jame
print("Minute =", a.minute)# ropen
print("Second =", a.second)# varkyane
print("Microsecond =", a.microsecond)# milivarkyane

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
# datetime.timedelta - nerkayacnum e tevoxutyun (day,hour:minute:second.microsecond)

# ogtagorcum enq date()
t1 = datetime.date(year=2018, month=7, day=12)
t2 = datetime.date(year=2017, month=12, day=23)

t3 = t1 - t2 # karanq amsatver irariv hanenq iraric hanenq

print("t3 =", t3, type(t3))# 201 days, 0:00:00 <class 'datetime.timedelta'>
print('datetime')

# ogtagorcum enq datetime()
t1 = datetime.datetime(2018, 7, 12, 7, 9, 33)
t2 = datetime.datetime(2019, 6, 10, 5, 55, 13)
t3 = t1 - t2
print("t3 =", t3, type(t3))# -333 days, 1:14:20 <class 'datetime.timedelta'>

#---------------------------------------------------

#karanq nayev ays tarberakov
t1 = datetime.timedelta(weeks=2, days=5, hours=1, seconds=33)
t2 = datetime.timedelta(days=4, hours=11, minutes=4, seconds=54)

t3 = t1 - t2

print("t3 =", t3)# 14 days, 13:55:39

#---------------------------------------------------

t = datetime.timedelta(days=5, hours=1, seconds=33, microseconds=233423)
print("Total seconds =", t.total_seconds())# 435633.233423
#talis e miayn varkyanerov

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#pythoni (datetime class)-i fromat
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

# masatvi yev jami nerkyacnman cevere shat tarber en tarber vayrerum ornak
# AMN-yum aveli taracac e (mm/dd/yyyy) isk Mec Britaanyayum aveli taracvac e (dd/mm/yy)

# himikva amsative yev jame
now = datetime.datetime.now()

t = now.strftime("%H:%M:%S")# yete verjaketeri texe dnel mi urish simvel tvere kabjanven ayd simvlov
print(t)# hour:minut:second

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")# amise,ore poqratar isk jame,ropen,varkyane,tarin mecatar
print("s1:", s1)# month/day/year hour:minut:second

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")# karanq mer uzac hertakanutyamb anel
print("s2:", s2)# day/month/year hour:minut:second

#---------------------------------------------------

# obyektneri sahmanere
# %Y - year[0001, ..., 2018, 2019, ..., 9999]
# %m - month[01, 02, ..., 11, 12]
# %d - day[01, 02, ..., 30, 31]
# %H - hour[00, 01, ..., 22, 23
# %M - minute[00, 01, ..., 58, 59]
# %S - second[00, 01, ..., 58, 59]

#---------------------------------------------------

date_string = "25 December, 2022"
print("date_string =", date_string)# 25 December, 2022

# ogtagorcum enq strptime() vorpisi 'date_string' darcnel amsativ
date_object = datetime.datetime.strptime(date_string, "%d %B, %Y")

print("date_object =", date_object)# 2018-06-21 00:00:00

#---------------------------------------------------
# yentadrenq menq ashxatum ent naxagci vra yev petq e cucadrenq amsative yev
# jame yev mez petq e ayl jamayin gotu jamanake yev amsative
# dra hamar kogtagorvenq pytZ module ayd xandire lucelu hamar

import pytz

local = datetime.datetime.now()
print(local.strftime("%m/%d/%Y, %H:%M:%S"))#(month/day/year, hour:minute:second) local jamanake

tz_y = pytz.timezone('Asia/Yerevan')
datetime_y = datetime.datetime.now(tz_y)
print(datetime_y.strftime("%m/%d/%Y, %H:%M:%S"))#(month/day/year, hour:minute:second) Yerevani jamanake

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.datetime.now(tz_London)
print(datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))#(month/day/year, hour:minute:second) Londoni jamanake

#---------------------------------------------------

# bolor qaxaqnere ays ciklov karaq gtnenq

#for tz in pytz.all_timezones:
#     print(tz)


#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#TIME
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

#time() funkciyan veradarcnum e darashrjanic ancac varkyanneri qanake
import time

#talis e darashrjanic ancac varkyanneri qanake
seconds = time.time()

print(seconds)# 1716651595.4086804

#---------------------------------------------------

#darashrjanis ancac varkyanere
seconds = 1716651595.4086804

# poxum e varkyanere entercvox cevachapi
l_time = time.ctime(seconds)

print(l_time)# Sat May 25 19:39:55 2024

#---------------------------------------------------

print('Hello')
time.sleep(2.4)# kagnacnum e hajord gorcoxutyune tvac varkyani chapov
print('World')

#---------------------------------------------------

result = time.localtime(1716651595)# trvac varkyanov hashvum e tarin amise ore yev ayln
print(result)# time.struct_time(tm_year=2024, tm_mon=5, tm_mday=25, tm_hour=19, tm_min=39, tm_sec=53, tm_wday=5, tm_yday=146, tm_isdst=0)
print(result.tm_year)# 2024
print(result.tm_hour)# 19

#---------------------------------------------------

# (year, month, day, hour, minute, second, weekday, day of the year, daylight saving)
time_t = (2024, 5, 25, 19, 39, 53, 5, 146, 0)

seconds = time.mktime(time_t)# poxum e varkyaneri

print(seconds)# 1716651595

#---------------------------------------------------

time_t = (2024, 5, 25, 19, 39, 53, 5, 146, 0)

print(time.asctime(time_t))# Sat May 25 19:39:53 2024


#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
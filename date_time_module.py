import datetime, time

print(datetime.datetime.now())

dt = datetime.datetime.now()
print("{}-{}-{}".format(dt.year, dt.month, dt.day))
print(("%s%s%s"%(dt.year, dt.month, dt.day)))

print(dt.hour, dt.minute, dt.second)

print(datetime.datetime.fromtimestamp(1000000))

print(datetime.datetime.fromtimestamp(time.time()))

halloween2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
newyears2020 = datetime.datetime(2020, 1, 1, 0, 0, 0)
oct31_2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)

assert(halloween2019 == oct31_2019)
# assert(halloween2019 > newyears2020) #false
assert(newyears2020 > halloween2019)

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta, 'microseconds :', delta.microseconds)

# adding 300 days
dt = datetime.datetime.now()
threehundred_days = datetime.timedelta(days=300)
print(dt + threehundred_days)

# 60 years back
oct21 = datetime.datetime(2019, 10, 21, 16, 29, 0)
about_thirty_years = datetime.timedelta(days=365*30)

prev_years_30 = oct21 - about_thirty_years
pre_year_60  = oct21 - (2 * about_thirty_years)
print('If there Mummy:', prev_years_30)
print('Mummy: ?', pre_year_60)

# Pausing Until a Specific Date
halloween2016 = datetime.datetime(2016, 10, 31, 0, 0, 0)
while datetime.datetime.now() < halloween2016:
    time.sleep(1)
    print('hull')

# important in datetime module
'''
strftime() directive
	

Meaning

%Y
Year with century, as in '2014'
%y
Year without century, '00' to '99' (1970 to 2069)
%m
Month as a decimal number, '01' to '12'
%B
Full month name, as in 'November'
%b
Abbreviated month name, as in 'Nov'
%d	
Day of the month, '01' to '31'
%j
Day of the year, '001' to '366'
%w
Day of the week, '0' (Sunday) to '6' (Saturday)
%A
Full weekday name, as in 'Monday'
%a
Abbreviated weekday name, as in 'Mon'
%H
Hour (24-hour clock), '00' to '23'
%I
Hour (12-hour clock), '01' to '12'
%M
Minute, '00' to '59'
%S
Second, '00' to '59'
%p
'AM' or 'PM'
%%
Literal '%' character
'''

oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))

print(oct21st.strftime('%I:%M %p'))
print(oct21st.strftime('%B of %y'))

'''
Converting Strings into datetime Objects
If you have a string of date information, such as '2019/10/21 16:29:00' or 'October 21, 2019', 
and need to convert it to a datetime object, use the datetime.datetime.strptime() function. 
The strptime() function is the inverse of the strftime() method. A custom format string using
the same directives as strftime() must be passed so that strptime() knows how to parse and
understand the string. (The p in the name of the strptime() function stands for parse.)
'''

newd = datetime.datetime.strptime('October 21, 2019', '%B %d, %Y')
print('Using strptime:- ', newd, type(newd))

newd1 = datetime.datetime.strptime('October of 19', '%B of %y')
print('Using strptime:- ', newd1)

newd2 = datetime.datetime.strptime('November of 63', '%B of %y')
print('Using strptime:- ', newd2)








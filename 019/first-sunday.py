#!/usr/bin/env python
months = [
    31,
    28,
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31
]

week = ['sun',
        'mon',
        'tue',
        'wed',
        'thu',
        'fri',
        'sat'
       ]

leapyears = [year for year in range(1, 101) if year % 4 == 0]

day = 0 # 1 Jan 1901
month = 0 # January
year = 1 # 1901
weekday = 2 # Tuesday

days = {day: week[weekday]} 

since_last_month = 0
since_last_year = 0

first_of_months = {}
while year <= 100:
    #print "%s/%s/%s - %s" % (month+1, since_last_month+1, year+1900, week[weekday])
    # if it's the first of the month, make a note 
    # of the weekday.
    if since_last_month == 0:
        first_of_months["%s/%s/%s" % (month+1, since_last_month+1, year+1900)] = week[weekday]

    # increment the counters..
    day += 1
    since_last_month += 1
    since_last_year += 1
    
    # check what year it is
    days_of_year = 365
    if year in leapyears:
        days_of_year += 1
    if since_last_year >= days_of_year:
        year += 1
        since_last_year = 0

    # check what month it is
    days_of_month = months[month]
    if month == 1 and year in leapyears: # february
        days_of_month += 1
    if since_last_month >= days_of_month:
        month += 1
        since_last_month = 0
        if month > len(months)-1:
            month = 0

    # check what day of the week it is
    weekday += 1
    if weekday > len(week)-1:
        weekday = 0
    days[day] = week[weekday]

def date_sort(date):
    date_str = date[0]
    month,day,year = date_str.split('/')
    return int(month)*int(day)*int(year)

print(len([weekday for weekday in list(first_of_months.values()) if weekday == 'sun']))

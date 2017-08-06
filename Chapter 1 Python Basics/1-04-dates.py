#!/usr/bin/env python3
from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta

# I. Print today's date, as well as the year, month, and day elements
today = date.today()
print("Output #41: today: {0!s}".format(today))
print("Output #42: {0!s}".format(today.year))
print("Output #43: {0!s}".format(today.month))
print("Output #44: {0!s}".format(today.day))
current_datetime = datetime.today()
print("Output #45: {0!s}".format(current_datetime))

# II. Calculate a new date using a timedelta
one_day = timedelta(days = -1)
yesterday = today + one_day
print("Output #46: yesterday: {0!s}".format(yesterday))
eight_hours = timedelta(hours = -8)
print("Output #47: {0!s} {1!s}"\
	.format(eight_hours.days, eight_hours.seconds))

# timedelta stores time differences inside the parentheses
# as days, seconds, and microseconds and then normalizes
# the values to make them unique
#
# timedelta(hours = -8) is timedelta(-1 days, 57,600 seconds)

# III. Calculate the number of days betweeen two dates
date_diff = today - yesterday
print("Output #48: {0!s}".format(date_diff))
print("Output #49: {0!s}".format(str(date_diff).split()[0]))

# IV. Create a string with a specific format from a date object
print("Output #50: {:s}".format(today.strftime('%m/%d/%Y')))
print("Output #51: {:s}".format(today.strftime('%b %d, %Y')))
print("Output #52: {:s}".format(today.strftime('%Y-%m-%d')))
print("Output #53: {:s}".format(today.strftime('%B %d, %Y')))

# %m %d %Y month day year in numeric form
# %m Month as a zero-padded decimal number
# %b Month as locale's abbreviated name
# %B Month as locale's full name
# %d Day of the month as a zero-padded decimal number.
# %y Year without century as a zero-padded decimal number.
# %Y Year with century as a decimal number.
# %a Weekday as locale's abbreviated name
# %A Weekday as locale's full name
# %w Weekday as decimal 0 ~ 6, 0 is Sunday and 6 is Saturday


# IV. Create a datetime objject with a specific format
# from a string representing a date

date1 = today.strftime('%m/%d/%Y')
date2 = today.strftime('%b %d, %Y')
date3 = today.strftime('%Y-%m-%d')
date4 = today.strftime('%B %d, %Y')

# Two datetime objects and two date objects based on
# the four strings that have different date formats

print("Output #54: {!s}".format(datetime.strptime(date1, '%m/%d/%Y')))
print("Output #55: {!s}".format(datetime.strptime(date2, '%b %d, %Y')))

print("Output #56: {!s}".format(datetime.date(datetime.strptime\
	(date3, '%Y-%m-%d'))))

print("Output #57: {!s}".format(datetime.date(datetime.strptime\
	(date4, '%B %d, %Y'))))
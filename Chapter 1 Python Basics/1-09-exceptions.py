#!/usr/bin/env python3

# Common Exceptions:
# - IOError
# - IndexError
# - KeyError
# - NameError
# - SyntaxError
# - TypeError
# - UnicodeError
# - ValueError

# I. try-except:
def getMean(numericValues):
	return sum(numericValues)/len(numericValues)
my_list2 = [ ]

try:
	print("Output #138: {}".format(getMean(my_list2)))
except ZeroDivisionError as detail:
	print("Output #138 (Error): {}"
		  .format(float('nan')))
	print("Output #138 (Error): {}".format(detail))

# II. try-except-else-finally
try:
	result = getMean(my_list2)
except ZeroDivisionError as detail:
	print("Output #142 (Error): " + str(float('nan')))
	print "Output #142 (Error):", detail
else:
	print "Output #142 (the mean is): ", result
finally:
	print("Output #142 (Finally): "
		  + "the finally block is executed every time")
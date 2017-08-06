#!/usr/bin/env python3
print("Output #1: I'm excited to learn Python.")

# Add two numbers together
x = 4
y = 5
z = x + y
print("Output #2: Four plus five equals {0:d}.".format(z))

# Add two lists together
a = [1, 2, 3, 4]
b = ["first", "second", "third", "fourth"]
c = a + b
print("Output #3: {0}, {1}, {2}".format(a, b, c))

# *****- Basic Data Types -*****
# ** Integers **
x = 9
print( "Output #4: {0}".format(x) )

print("Output #5: {0}".format(3**4))
# result: 81, 3**4 "raise the number 3 to the power of 4"

print("Output #6: {0}".format(int(8.3) / int(2.5)))
# it doesn't matter if there are spaces between ()
# and the content enclosed

# ** Floating-Point Numbers **
# Numbers with Decimal Points

print("Output #7: {0:.3f}".format(8.3/2.7))
# Output #7: 3.074

y = 2.5*4.8
print("Output #8: {0:.1f}".format(y))
# Output #8: 12.0

r = 8/float(3)
print("Output #9: {0:.2f}".format(r))
print("Output #10: {0:.4f}".format(8.0/3))
# Output #9: 2.67
# Output #10: 2.6667

print( type(y) )
# <type 'float'>

# *** Strings ***
print("Output #14: {0:s}".format('I\'m enjoying learning Python.'))

print("Output #15: {0:s}".format("This is a long string. Without the backslash\
it would run off of the page on the right in the text editor and be very\
difficult to read and edit. By using the backslash you can split the long\
string into smaller strings on separate lines so that the whole string is easy\
to view in the text editor."))

print("Output #16: {0:s}".format('''You can use triple single quotes

for multi-line comment strings.'''))

print("Output #17: {0:s}".format("""You can also use triple double quotes

for multi-line comment strings."""))

# basic operation with Strings
# + * len()
string1 = "This is a "
string2 = "short string."
sentence = string1 + string2
print("Output #18: {0:s}".format(sentence))
print("Output #19: {0:s} {1:s}{2:s}".format("She is", "very "*4, "beautiful."))
m = len(sentence)
print("Output #20: {0:d}".format(m))

# split([sep[, maxsplit]])
string1 = "My deliverable is due in May"

# Default, any whitespace char is a separator,
# the string is separated into words in an array
string1_list1 = string1.split()

# sep: where the split should happen
# maxsplit: maximum split count
string1_list2 = string1.split(" ", 2)
print("Output #21: {0}".format(string1_list1))
print("Output #22:\
	\n    First Piece: {0}\n    Second Piece: {1}\n    Third Piece: {2}"\
	.format(string1_list2[0], string1_list2[1], string1_list2[2]))

string2 = "Your,deliverable,is,due,in,June"
string2_list = string2.split(",")
print("Output #23: {0}".format(string2_list))
print("Output #24: {0} {1} {2}".format(string2_list[1], string2_list[5],\
	string2_list[-1]))
# in Python, iteration index can be negative, it just means count backwards
# so -n mean the (n-1)th item from last, -1 means the last item

# join()
print("Output #25: {0}".format( ",".join(string2_list)))

# strip
# strip([chars]): remove chars from both sides of the string
# lstrip([chars]): remove chars from the leading side of the string
# rstrip([chars]): remove chars from the trailing side of the string
#
#
# The chars argument is a string specifying the set of c
# haracters to be removed. If omitted or None, the chars
# argument defaults to removing whitespace.

# Removing whitespaces
string3 = " Remove  unwanted characters from this string. \t\t   \n"
print("Output #26: string3:{0:s}".format(string3))

string3_lstrip = string3.lstrip()
print("Output #27 string3_lstrip:{0:s}".format(string3_lstrip))

string3_rstrip = string3.rstrip()
print("Output #28 string3_rstrip:{0:s}".format(string3_rstrip))

string3_strip = string3.strip()
print("Output #29 string3_strip:{0:s}".format(string3_strip))

# Removing other characters
string4 = "$$Unwanted characters.__---+++"
print("Output #30: string4:{0:s}".format(string4))

string4_strip = string4.strip("$_-+.")
print("Output #31: string4_strip:{0:s} has been removed.".format(string4_strip))

# replace
string5 = "Let's replace the spaces in this sentence with other characters."
string5_replace = string5.replace(" ", "!@!")
print("Output #32 string3_lstrip:{0:s}".format(string5_replace))

# Changing Cases
# lower(), upper(), capitalize()
#
# capitalize() function applies upper() to the first character in each word,
# lower() to the remaining characters



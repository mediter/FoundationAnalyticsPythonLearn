#!/usr/bin/env python3
from math import exp, log, sqrt
import re

# I. Count the number of times a pattern appears in a string
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()

pattern = re.compile(r"The", re.I)
# compiling regular expression:
#     NOT Always necessary,
#     but it can significantly increase a program's speed
count = 0
for word in string_list:
	if pattern.search(word):
		count += 1
print("Output #38: {0:d}".format(count))

# II. Print the pattern each time it is found in the string
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"(?P<match_word>The)", re.I)
# (?P<match_word>The) is a capture group
# it can be later referred to as match_word
#
# But what does "</match_word>" at the end of line do?
# syntax error, can confirm it is an error possibly
# created by format conversion

print("Output #39:")
for word in string_list:
	if pattern.search(word):
		print( "{:s}".format(pattern.search(word).group('match_word')))

# III. Substitute the letter "a" for the world "the" in the string
string = "The quick brown fox jumps over the lazy dog."
string_to_find = r"The"
pattern = re.compile(string_to_find, re.I)
print("Output #40: {:s}".format(pattern.sub("a", string)))


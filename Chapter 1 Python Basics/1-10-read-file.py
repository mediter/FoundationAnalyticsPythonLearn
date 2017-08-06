#!/usr/bin/env python3
import sys

# Importing the sys module puts the argv list variable
# argv: the list of command-line arguments
# - argv[0] the script name
# - argv[1] the first additional argument passed
#           to the script on the command line

# READ A FILE
# Read a single text file
#
# the legacy way
input_file = sys.argv[1]

print("Output #143: ")
filereader = open(input_file, 'r')
for row in filereader:
    print(row.strip())
filereader.close()

# Modern File-Reading Syntax
# available in Python version > 2.5
#
# using "with as" syntax, no need to use close()
# file is automatically closed when the
# with-statements exits.
input_file = sys.argv[1]
print("Output #144:")
with open(input_file, 'r', newline='\n') as filereader:
    for row in filereader:
        print("{}".format(row.strip()))

# open(input_file, 'r', newline='\n')
# is Python 3 syntax

#!/usr/bin/env python3
import sys

# Writing to a Text File
#
# write()
# writes individual strings to a file
#
# writelines()
# writes a sequence of strings to a file

# Write to a Text File
my_letters = ['a', 'b', 'c', 'd', 'e',
              'f', 'g', 'h']
max_index = len(my_letters)
output_file = sys.argv[1]
filewriter = open(output_file, 'w')
for index_value in range(max_index):
    if index_value < (max_index - 1):
        filewriter.write(my_letters[index_value] + '\t')
    else:
        filewriter.write(my_letters[index_value] + '\n')
filewriter.close()
print("Output #146: Output written to file")

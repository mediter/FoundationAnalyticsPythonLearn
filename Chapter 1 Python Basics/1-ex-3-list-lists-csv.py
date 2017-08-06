#!/usr/bin/env python3
import sys

list_combined = [
    ['a', 'b', 'c', 'd'],
    ['apple', 'mangosteen', 'durian', 'mango'],
    [23, 34, 128, 97]
]

output_file = sys.argv[1]
filewriter = open(output_file, 'a')

for index_a in range(len(list_combined)):
    temp_list = list_combined[index_a]
    max_index = len(temp_list)

    for index_b in range(max_index):
        if index_b < max_index - 1:
            filewriter.write(
                str(temp_list[index_b]) + ",")
        else:
            filewriter.write(
                str(temp_list[index_b]) + "\n")

filewriter.close()
print("Output appended to file")

#!/usr/bin/env python3
import sys
import glob
import os

# I. Reading Multiple Text Files with glob
print("Output #145:")
inputPath = sys.argv[1]
for input_file in\
        glob.glob(os.path.join(inputPath, '*.txt')):
    with open(input_file, 'r') \
            as filereader:
        for row in filereader:
            print("{}".format(row.strip()))
    print("\n")

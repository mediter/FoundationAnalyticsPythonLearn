#!/usr/bin/env python3
from operator import itemgetter

# I. sort
# sort simple list
unordered_list = [3, 5, 1, 7, 8, 0, 9, 2]
print("Output #88: {}".format(unordered_list))

list_copy = unordered_list[:]
list_copy.sort()
print("Output #89: {}".format(list_copy))
print("Output #90: {}".format(unordered_list))

# II. sorted
# sort a list that contains lists
my_lists = [[1, 2, 3, 4], [4, 3, 2, 1], [3, 6, 9, 12]]
my_lists_sorted_by_index_3 = sorted(my_lists, key=lambda
                                    index_value: index_value[3])
print("Output #91: {}".format(my_lists_sorted_by_index_3))

# III. itemgetter
# the operator module provides functionality for sorting
# lists, tuples, and dictionaries by multiple keys.

my_lists = [[123, 2, 3, 445], [22, 6, 6, 444], [354, 4, 4, 689],
            [236, 5, 5, 621], [578, 1, 1, 9989], [461, 1, 1, 290]]

my_lists_sorted_by_index_3_and_0 = sorted(my_lists, key=itemgetter(3, 0))
print("Output #92: {}".format(my_lists_sorted_by_index_3_and_0))

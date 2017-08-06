#!/usr/bin/env python3

# List comprehension
my_data = [[1,2,3], [4,5,6], [7,8,9]]
rows_to_keep = [row for row in my_data if row[2] > 5]
print("Output #130 (list comprehension): {}"
	  .format(rows_to_keep))

# Set comprehension
my_data = [(1,2,3), (4,5,6), (7,8,9), (7,8,9)]
set_of_tuples1 = {x for x in my_data}
print("Output #131 (set comprehension): {}"
	  .format(set_of_tuples1))
set_of_tuples2 = set(my_data)
print("Output #132 (set function): {}"
	  .format(set_of_tuples2))

# Dictionary comprehension
my_dictionary = {
                 'customer1': 7,
                 'customer2': 9,
                 'customer3': 11
                }
my_results = {key : value for key, value in
              my_dictionary.items() if value > 10}
print("Output #133 (dictionary comprehension): {}"
	  .format(my_results))
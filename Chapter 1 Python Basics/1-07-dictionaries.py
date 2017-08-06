#!/usr/bin/env python3

# Dictionaries

# I. Create Dictionaries
# Use curly braces to create a dictionary
# Use a colon between keys and values in each pair
#
# len() counts the number of key-value pairs in a
# dictionary

empty_dict = {}
a_dict = {'one': 1, 'two': 2, 'three': 3}
print("Output #102: {}".format(a_dict))
print("Output #103: a_dict has {!s} elements"
      .format(len(a_dict)))
# why use {!s} to force convert int to string?

print(type(len(a_dict)))

# Add elements to a dictionary
a_dict.update({'item3': 3})
a_dict["whatever"] = 6996

# II. Access a value in a dictionary
# Use keys to access specific values in a dictionary

print("Output #106: {}".format(a_dict['two']))

# III. copy()
a_new_dict = a_dict.copy()
print("Output #108: {}".format(a_new_dict))

# IV. keys, values, and items
# use keys(), values(), and items() to access
# a dictionary's keys, values, and key-value
# pairs respectively
print("Output #109: {}".format(a_dict.keys()))
print("Output #111: {}".format(a_dict.values()))
print("Output #112: {}".format(a_dict.items()))

# The result is a list of key-value pair tuples.
# For example, the result of a_dict.items() is
# [('three', 3), ('two', 2), ('one', 1)]

# V. in, not in, and get

if 'two' in a_dict:
    print("Output #114: two is a key in a_dict: {}"
          .format(a_dict.keys()))
print("Output #116: {!s}".format(a_dict.get('three')))
print("Output #117: {!s}".format(a_dict.get('four')))
print("Output #118: {!s}".format(a_dict.get
      ('four', 'Not in dict')))
# get() can take 1 or 2 parameters
# - if 1 parameter and it is not in the dictionary,
#   the return value would be None
# - if 2 parameters and the first parameter is not
#   in the dictionary, the returned value would be
#   the second parameter


# VI. Sorting
# Use sorted() to sort a dictionary

print("Output #119: {}".format(a_dict))

dict_copy = a_dict.copy()
ordered_dict1 = sorted(dict_copy.items(), key=lambda
                       item:item[0])
print("Output #120 (order by keys): {}"
      .format(ordered_dict1))
# dict_copy.items()
# -> [('three', 3), ('two', 2), ('one', 1)]
# why item:item[0] instead of (item, item)?
# item:item[0] means item[0] in item

ordered_dict2 = sorted(dict_copy.items(), key=lambda
                       item:item[1])
print("Output #121 (order by values): {}"
      .format(ordered_dict2))

ordered_dict3 = sorted(dict_copy.items(), key=lambda
                       x:x[1], reverse=True)
print("Output #122 (order by values, descending): {}"
      .format(ordered_dict3))

ordered_dict4 = sorted(dict_copy.items(), key=lambda
                       x:x[1], reverse=False)
print("Output #123 (order by values, descending): {}"
      .format(ordered_dict4))

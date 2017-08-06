#!/usr/bin/env python3

# Tuples

# I. Create Tuples
# use parentheses to create a tuple
my_tuple = ('x', 'y', 'z')
print("Output #93: {}".format(my_tuple))
print("Output #94: my tuple has {} elements.".format(len(my_tuple)))
print("Output #95: {}".format(my_tuple[1]))

longer_tuple = my_tuple + ('car', 'truck', 'ferry')
print("Output #96: {}".format(longer_tuple))

# II. Unpack tuples
one, two, three = my_tuple
print("Output #97: {0} {1} {2}".format(one, two, three))

var1 = 'red'
var2 = 'robin'
print("Output #98: {} {}".format(var1, var2))

var1, var2 = var2, var1
print("Output #99: {} {}".format(var1, var2))
# treated as two tuples even though there are no parentheses

# III. Convert tuples to lists (and vice versa)
my_list = [1, 2, 3]
my_tuple = ('x', 'y', 'q')
print("Output #100: {}".format(tuple(my_list)))
print("Output #101: {}".format(list(my_tuple)))

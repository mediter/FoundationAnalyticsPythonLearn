#!/usr/bin/env python3

# *****- Lists -*****
# - ordered collections of objects
# - can contain objects of different types

# I. Create a List
# - use square brackets to create a list
# - len() the number of elements in a list
# - min() / max()
# - count() the number of times a value appears in a list

a_list = [1, 3, 5]

print("Output #58: {}".format(a_list))
print("Output #59: a_list has {} elements.".format(len(a_list)))
print("Output #60: the maximum value in a_list is {}.".format(max(a_list)))
print("Output #61: the minimum value in a_list is {}.".format(min(a_list)))

another_list = ['printer', 5, ['stats', 'circle', 9]]

print("Output #62: another_list has {} elements.".format(len(another_list)))
print("Output #63: 5 appears in another_list {} times.".format
      (another_list.count(5)))

# between parentheses, the backslash is not necessary
# for indicating line-continuation

# II. Use index values to access the specific elements in a list
# [0] is the first element; [-1] is the last element

print("Output #65: {}".format(a_list[0]))
print("Output #66: {}".format(a_list[1]))
print("Output #67: {}".format(a_list[2]))
print("Output #68: {}".format(a_list[-1]))
print("Output #69: {}".format(a_list[-2]))
print("Output #70: {}".format(a_list[-3]))

# III. List Slices
# - Use list slices to access a subset of list elements
# - No starting index means start from the beginning
# - No ending index means run all the way to the end

print("Output #73: {}".format(a_list[0:2]))
print("Output #74: {}".format(another_list[:2]))
print("Output #75: {}".format(a_list[1:3]))
print("Output #76: {}".format(another_list[1:]))

# does not include the element at the end index


# IV. Copy a list
# use list_name[:]
a_list_copy = a_list[:]
print("Output #77: {}".format(a_list_copy))

# if a_list_copy is modified, a_list stay unchanged
# if a_list_copy = a_list, they change together

# V. Concatenate a list
# use + in between two or more lists
a_longer_list = a_list + another_list
print("Output #78: {}".format(a_longer_list))

# VI. "in" and "not in"
# check whether specific elements are or are not in a list
a = 2 in a_list
print("Output #79: {}".format(a))

if 2 in a_list:
    print("Output #80: 2 is in {}".format(a_list))

b = 6 not in a_list
print("Output #81: {}".format(b))
if 6 not in a_list:
    print("Output #82: 6 is not in {}.".format(a_list))

# VII. append remove pop
# - append() add additional elements to the end of the list
# - remove() remove specific elements from the list
# - pop()    remove a single element from the end of the list
a_list.append(4)
a_list.append(5)
a_list.append(6)
print("Output #83: {}".format(a_list))

a_list.remove(5)
print("Output #84: {}".format(a_list))

a_list.pop()
a_list.pop()
print("Output #85: {}".format(a_list))

# VIII. reverse
# reverse() reverse a list in-place
a_list.reverse()
print("Output #86: {}".format(a_list))

a_list_copy = a_list[:]
a_list_copy.reverse()
print("Output #87: {} reversed is {}".format(a_list, a_list_copy))



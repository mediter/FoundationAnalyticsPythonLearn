#!/usr/bin/env python3

list_alpha = ['a', 'b', 'c', 'd']
list_num = [23, 36, 187]
list_fruit = ['apple', 'mangosteen',
              'durian', 'mango']
list_combined = list_alpha + list_num + list_fruit

for index_value in range(len(list_combined)):
    print("The element at index: {:02d} is {}"
          .format(index_value, list_combined[index_value]))

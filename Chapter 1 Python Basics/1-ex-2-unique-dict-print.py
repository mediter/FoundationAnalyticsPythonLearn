#!/usr/bin/env python3

list_alpha = ['a', 'b', 'c', 'd']
list_fruit = ['apple', 'mangosteen',
              'durian', 'mango']
result_dict = {}
print("The final dictionary contains:")
for index_value in range(len(list_alpha)):
    if list_alpha[index_value] in result_dict:
        continue
    else:
        result_dict.update({list_alpha[index_value]: list_fruit[index_value]})
        print("{} : {}"
              .format(list_alpha[index_value],
                      list_fruit[index_value]))

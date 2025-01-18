"""
In this kata you will create a function that takes a list of non-negative integers and 
strings and returns a new list with the strings filtered out.

Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

"""

# Declare a the new list
new_list = []

def filter_list(l):
    'return a new list with the strings filtered out'
    old_list = l
    # Declare elements to append to the new list after filtering
    filtered_elements = [x for x in old_list if type(x) == int]
    # Return the filtered elements
    return filtered_elements

print(filter_list([1,2,'a','b']))

"""
Given two integers a and b, which can be positive or negative, 
find the sum of all the integers between and including them and return it. 
If the two numbers are equal return a or b.

Note: a and b are not ordered!

Examples (a, b) --> output (explanation)
(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)

"""


def get_sum(a,b):
    """Given two integers a and b, which can be positive or negative, 
    find the sum of all the integers between and including them and return it. 
    If the two numbers are equal return a or b.
    """
    # Arrange a and b in ascending order
    ab_list = [a, b]
    if a > b:
        ab_list = [b, a]
        
        total_sum = sum(range(ab_list[0], (ab_list[-1]+1)))
    elif a < b:
        
        total_sum = sum(range(ab_list[0], (ab_list[-1]+1)))
    
    elif a == b:
        total_sum = a
        

    return total_sum
    

    # Loop through all numbers in the range between a, and b, and add them


print(get_sum(-1, 0))

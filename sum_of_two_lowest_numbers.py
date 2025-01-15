"""
Create a function that returns the sum of the two lowest positive numbers given 
an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455

"""

def sum_two_smallest_numbers(numbers):
    #your code here
    """ 
    A function that returns the sum of the two lowest positive numbers given 
    an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

    """
    # Find the first minimum number
    minimum1 = min(numbers)
    # Remove it from the list
    minimum1_index = numbers.index(minimum1) # find the index of minimum1
    removed_minimum1 = numbers.pop(minimum1_index) # extract the number and assign it to a variable, removed_minimum1

    minimum2 = min(numbers)
    minimum2_index = numbers.index(minimum2) # find the index of minimum1
    removed_minimum2 = numbers.pop(minimum2_index)

    # Sum the two minimum numbers
    sum = removed_minimum1 + removed_minimum2

    return sum


print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]))


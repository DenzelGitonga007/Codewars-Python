"""
Write an algorithm that takes an array and moves all of the zeros to the end, 
preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

"""

def move_zeros(lst):
    """
    Takes an array and moves all of the zeros to the end, 
    preserving the order of the other elements.

    """
    # Create the list to hold the zeros and another to hold the non-zero numbers
    non_zeros = [num for num in lst if num != 0]
    zeros = [num for num in lst if num == 0]

    lst = non_zeros + zeros

    return lst

print(move_zeros([9, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0]))
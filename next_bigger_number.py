"""
Create a function that takes a positive integer and returns the next bigger number 
that can be formed by rearranging its digits. For example:

  12 ==> 21
 513 ==> 531
2017 ==> 2071
If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift, None in Rust):

  9 ==> -1
111 ==> -1
531 ==> -1

"""

def next_bigger(n):
    """
    A function that takes a positive integer and returns the next bigger number 
    that can be formed by rearranging its digits.

    """
    # Set the n to be a list of the digits
    raw_list = list(str(n))
    bigger_number_list = [] # the list to append the newly rearranged numbers
    # Pop the max numbers and append them onto another list to form the bigger number
    while len(raw_list) > 0: # until the raw list is empty
        biggest_digit = max(raw_list)
        bigger_number_list.append(biggest_digit) # append the number to the bigger number list
        raw_list.remove(biggest_digit) # remove the digit from the raw list
    
    # Combine the bigger number list, into one digit

    bigger_number = int(''.join(bigger_number_list))

    # Return -1 if the number is same as the original one
    if bigger_number == n:
        return -1
    else:
        return bigger_number
        

    pass

print(next_bigger(111))
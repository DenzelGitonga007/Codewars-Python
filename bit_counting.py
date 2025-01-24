"""
Write a function that takes an integer as input, and returns the number of bits that are 
equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

"""

def count_bits(n):
    """
    A function that takes an integer as input, and returns the number of bits that are 
    equal to one in the binary representation of that number. You can guarantee that input is non-negative.

    """
    # Convert the number to it's binary form, and append to a list
    bit_num = list(bin(n)[2:]) # range 2+ removes the 'ob' prefix from the number
    # Count how many times 1 appears
    bit_count = bit_num.count('1') 
    return bit_count

print(count_bits(1234))
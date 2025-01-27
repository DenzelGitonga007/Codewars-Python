"""
Given the string representations of two integers, return the string representation of the sum of those integers.

For example:

sumStrings('1','2') // => '3'
A string representation of an integer will contain no characters besides the ten numerals "0" to "9".

I have removed the use of BigInteger and BigDecimal in java

Python: your solution need to work with huge numbers (about a milion digits), converting to int will not work.

"""

def sum_strings(x, y):
    """
    Given the string representations of two integers, return the string representation of the sum of those integers.

    """

    sum = int(x) + int(y)
    string_sum = str(sum)

    return string_sum

    # return "42"

print(sum_strings('1','2'))

"""
Find the missing letter
Write a method that takes an array of consecutive (increasing) letters as input and 
that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. 
The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
(Use the English alphabet with 26 letters!)

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have also created other katas. Take a look if you enjoyed this kata!

"""

import string # get the alphabets module

def find_missing_letter(chars):
    """
    A method that takes an array of consecutive (increasing) letters as input and 
    that returns the missing letter in the array.

    """

    alphabets = list(string.ascii_letters)#get the alphabets from the string module, irregardless of the case, and put them in a list
    # Obtain the alphabets from chars, in alphabets
    start_index = alphabets.index(chars[0]) # start index of the chars alphabets
    end_index = alphabets.index(chars[-1]) + 1
    # Append the complete set of letters onto a new list
    complete_letters = alphabets[start_index:end_index]
    for letter in complete_letters:
        if letter not in chars:
            missing_letter = letter
    

    return missing_letter

print(find_missing_letter(['O','Q','R','S']))

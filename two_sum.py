"""
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
which is the number of times you must multiply the digits in num until you reach a single digit.

For example (Input --> Output):

39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit, there are 3 multiplications)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2, there are 4 multiplications)
4 --> 0 (because 4 is already a one-digit number, there is no multiplication)

"""

def persistence(n):
    # your code
    """
    A function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
    which is the number of times you must multiply the digits in num until you reach a single digit.

    """

    # Set the condition/loop for when n is not more than one digit
    list_num = list(str(n)) # let the number be a list, to check individual digits   
    count = 0 # set count of how many times the multiply is done
    while len(list_num) > 1: # Check if the number is one digit long
        # Multiply all the elements in the list
        multiply = int(list_num[0]) * int(list_num[1])
        count += 1 # increment count
        list_num = list(str(multiply)) # let the new value (multiply), be the new item on the list
        
        print(multiply)
        # break
    print("How many times the multiplication has occured {}".format(count))

     
        

print(persistence(39))
        

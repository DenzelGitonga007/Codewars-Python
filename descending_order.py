""" 
Your task is to make a function that can take any non-negative integer as an argument
and return it with its digits in descending order. 
Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321

"""


# Function to welcome the user
def welcome():
    print("...Welcome to Denzel Descending Order App...")
    print(" ")
    print("You are to enter a positive number and then the program will rearrage its digits in descending order, to create the highest number possible")
    return " " # to avoid it from printing "None"

print(welcome())

# Create a loop to let the user enter a positive integer
while True:
    try:
        # Get the user input
        user_input = int(input("Enter the positive number you'd like to test out: "))
        if user_input >= 0:
            # Break the loop and proceed to break it down 
            print("Great, you entered {}, now let's work on it".format(user_input))
            break
        else:
            print("Oops! You have entered a negative number...")
            print("Please try again...")
    except ValueError:
        print("Oops! The value you entered is not a valid number, please try again with a valid number")


# def descending_order(num):
#     # Bust a move right here
#     return
    
# result = descending_order(user_input)
"""

Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

   12 --> "10 + 2"
   45 --> "40 + 5"
70304 --> "70000 + 300 + 4"
NOTE: All numbers will be whole numbers greater than 0.

"""

def expanded_form(num):
    # Convert the number to a string to access each digit
    num_str = str(num)
    
    # Create an empty list to store the expanded parts
    expanded_parts = []
    
    # Get the length of the number (to determine place values)
    length = len(num_str)

    # Loop through each digit in the number
    for i, digit in enumerate(num_str):
        if digit != '0':  # Ignore zeros, as they don't contribute to the expanded form
            # Calculate the place value (e.g., 7 in 70304 is 70000)
            place_value = int(digit) * (10 ** (length - i - 1))
            expanded_parts.append(str(place_value))  # Store as a string for joining later

    # Join the parts with " + " to return the final result
    return " + ".join(expanded_parts)


print(expanded_form(70304))
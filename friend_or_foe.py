"""
Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! 
Otherwise, you can be sure he's not...

Input = ["Ryan", "Kieran", "Jason", "Yous"]
Output = ["Ryan", "Yous"]

Input = ["Peter", "Stephen", "Joe"]
Output = []


"""


def friend(x):
    #Code
    """
    Filters a list of strings and returns a list with only your friends name in it.
    If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! 
    Otherwise, you can be sure he's not...

    """
    # Initialize the list
    names_list = x
    # Initialize a list to store the names of the friends with four letter names
    friends = []
    # Loop through the words to check if anyone of them is 4 letters
    for name in names_list:
        if len(name) == 4:
            friends.append(name)
    

    return friends

print(friend(["Peter", "Stephen", "Joe"]))


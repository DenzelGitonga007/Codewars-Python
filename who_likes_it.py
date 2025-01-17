"""
You probably know the "like" system from Facebook and other pages. 
People can "like" blog posts, pictures or other items. We want to create the text that 
should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. 
It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

"""


def likes(names):
    # your code here
    """
    Implement the function which takes an array containing the names of people that like an item. 
    It must return the display text

    """
    likes = names
    other_likes = [] # to store the other likes not given names
    
    # Conditions
    if len(likes) == 0:
        return "no one likes this"
    elif len(likes) == 1:
        return "{} likes this".format(likes[0])
    elif len(likes) == 2:
        return "{} and {} like this".format(likes[0], likes[1])
    
    elif len(likes) == 3:
        return "{}, {} and {} like this".format(likes[0], likes[1], likes[2])
    elif len(likes) > 3:
        # Split the list from the second element, and put them in another list for counting
        other_likes = [other_likes.append(like) for like in range(2, len(likes))]
        # Count how many they are and print
        return "{}, {} and {} others like this".format(likes[0], likes[1], len(other_likes))
        
    pass


print(likes(["Alex", "Jacob", "Mark", "Max"]))
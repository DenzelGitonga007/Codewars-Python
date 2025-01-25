"""
Given an array (arr) as an argument complete the function countSmileys that 
should return the total number of smiling faces.

Rules for a smiling face:

Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
Every smiling face must have a smiling mouth that should be marked with either ) or D
No additional characters are allowed except for those mentioned.

Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]

Example
countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
Note
In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). 
Order of the face (eyes, nose, mouth) elements will always be the same.

"""


def count_smileys(arr):
    """
    Given an array (arr) as an argument complete the function countSmileys that 
    should return the total number of smiling faces.

    """
    # Set the valid smiles
    smiles = [':)', ':D', ':-)', ':-D', ';-)', ';-D', ':~D', ':~)', ';~D', ';)', ';D']
    # Append the common smiles found onto a list
    found_smiles = [valid_smiles for valid_smiles in arr if valid_smiles in smiles]
    # Return the count of the list of the common smiles
    if len(arr) == 0:
        return 0 # in case the array is empty
    else:
        return len(found_smiles)
    pass #the number of valid smiley faces in array/list

print(count_smileys([':D',':~)',';~D',':)']))
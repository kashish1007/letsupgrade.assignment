# Question 1
# Delete all occurrences of an element in a list

list_1 = [1,2,3,4,4,5,5,6,7,8,8]
print(set(list_1))

# Question 2
# Check whether a string is a pangram.

import string


def pangram(text):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for x in alpha:
        if x not in text.lower():
            return False

    return True


text = "hvuygihpihjp"

if pangram(text) == True:
    print("Yes")
else:
    print("No")

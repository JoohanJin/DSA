'''
Implement and algorithm to determine if a string has all unique characters.
Additional data structures cannot be used
'''

'''
Questions to think about:
    - If the string is an ASCII string or a Unicode String.
    - is it UTF-7? UTF-8? UTF-16 or UTF-32?
'''

# Assume that we are using extended ASCII, UTF-8
# we can create an array of boolean values, where the flag at index i indicates whether character i in the alphabet is contained in the string or not.
# The second time we see this character, we can immediately return False

# Using Pigeonhall Theorem, we can also immediately return False if the string length exceeds the number of unique characters in the alphabet.

# Time Complexity: O(n) where n is the length of the string
# we also can argue that the time complexity is O(1) since the loop will not iterate through more than 256 characters.
# Space Complexity: O(1)

def isUniqueCharSet(s: str):
    if (len(s) > 256): # pigeon hall theorem
        return False
    
    char_set = [0] * 256
    for i in s:
        val: int = ord(i)
        if (char_set[val]):
            return False
        char_set[val] = 1
    return True

'''
# Alternative Approaches
1. Comapre every character of the string to every other character of the string. This will take O(n^z) time complexity and O(1) space
2. If we are allowed to modify the input string, we could sort the string in O(n log n) time and then linearly check the string for
   neighboring characters that are identical. But extra space complexity expected.
'''
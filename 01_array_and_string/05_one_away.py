import sys
import math
'''
There are three types of edits that can be performed on strings:
- insert a character
- delete a character
- replace a character
Given two strings, write a function to check if they are one edit (or zero edits) away

e.g.
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bae -> false
'''

'''
possible solution:
- make a use of brute-force
    - generate or check the condition for a string from one edit away only
    - and compare with the editted str
'''

def one_replace_away(first: str, second: str):
    one_already_editted: bool = False
    for i in range(len(first)):
        if (first[i] != second[i]):
            if (one_already_editted):
                return False
            one_already_editted = True
    return True


def one_insertion_away(s1:str, s2: str):
    # s2 is longer
    i1: int = 0
    i2: int = 0

    while (i1 < len(s1) and i2 < len(s2)):
        if (s1[i1] != s2[i2]):
            if (i1 != i2):
                return False
            i2 += 1
        else:
            i1 += 1
            i2 += 1
    return True


def one_edit_away(first: str, second: str):
    if (len(first) == len(second)):
        return one_replace_away(first, second)
    elif (len(first) + 1 == len(second)): # insertion
        return one_insertion_away(first, second)
    elif (len(first) - 1 == len(second)): # deletion
        return one_insertion_away(second, first)
    return False


# TODO: implement merged one_edit_away
def one_edit_away_merged(first: str, second: str): 
    if (abs(len(first) - len(second)) > 1): return False
    same_len: bool = False

    # let's suppose that s1 is longer
    if (len(first) >= len(second)):
        s1, s2: str = first, second
    else:
        s1, s2: str = second, first

    i1, i2: int = 0, 0
    found_difference: bool = False


    while (i1 < len(s1) and i2 < len(s2)):
        return


if __name__=="__main__":
    first, second: str = sys.argv[1], sys.argv[2]
    print(one_edit_away(first, second))

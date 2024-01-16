'''
Check Permutation: Given two strings, write a method to decide if one is a permutation of the other
Observation 
1. Strings of different lengths cannot be permutations of each other.
'''

# Possible Solutions
'''
1. Sort the string
If two strings are permutations then we know that they have the same characters, but in different orders.
Therefore, sorting the strings will put the characters from two permutations in the same order.
We just need to compare the sorted versions of the strings.

not optimal, but clean and easy to understand.
'''
def check_permu_sort(s: str, t: str):
    if (len(s) != len(t)):
        return False
    
    s.sort()
    t.sort()

    return s == t


'''
2. Check if the two strings have identical character counts
We can also use the definition of a permutation - two words with the same character counts- to implement the algorithm.
We simply iterate through the given string, counting how many times each character appears. Then afterwards, we compare the two arrays
'''

def check_permu_count(s: str, t: str):
    if (len(s) != len(t)):
        return False
    
    char_set = [0] * 256 # assume that character set is ASCII

    for i in s: 
        char_set[ord(i)] = char_set[ord(i)] + 1

    for i in t:
        char_set[ord(i)] = char_set[ord(i)] - 1
        if (char_set[ord(i)] < 0):
            return False
    
    return True
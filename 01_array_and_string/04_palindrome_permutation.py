'''
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words
'''

'''
possible assumptions
- UTF-8? 256 chars
- or ASCII? 128 chars

Possible Solution 1
construct the hash table using ord() in python
iterate through the hash table and decide if there are more than one characters with odd number count.

Time Complexity: O(n)
'''
def isPalindrome(s: str):
    s: str = s.lower().replace(" ", "")
    found_odd: bool = False
    s_list: list[int] = [0] * 26

    # ord(char) - 97
    for i in s:
        s_list[ord(i) - 97] += 1

    for i in s_list:
        if (i % 2):
            if (found_odd):
                return False
            found_odd = not found_odd

    return True







if __name__ == "__main__":
    a = "Tact Coa"
    print(isPalindrome(a))

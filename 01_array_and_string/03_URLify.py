'''
URLify: Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end of to hold the additional characters,
and that you are given the "true" length of the string
'''

'''
possible solution

'''
# we have the buffer at the end of the stirng.
def URLify(s: list[str], true_length: int):
    space_count: int = 0
    for i in range(true_length):
        if (s[i] == " "):
            space_count += 1
    
    length: int = true_length + (2 * space_count)

    for i in range(true_length - 1, -1, -1):
        if (s[i] == " "):
            s[length - 1] = "0"
            s[length - 2] = "2"
            s[length - 3] = "%"
            length = length - 3
        else:
            s[length - 1] = s[i]
            length = length - 1
    return

if __name__ == "__main__":
    a = list("Mr John Smith    ")
    URLify(a, 13)
    print(a)
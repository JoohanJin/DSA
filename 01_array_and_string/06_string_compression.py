'''
String Compression 
Implement a method to perform basic string compression using the counts repeated characters.
For example, string "aabcccccaaa" would become a2b1c5a3.
If the compressed string would not become smaller than the original string, your method should return the original string.
You can assume the string only has only uppercase and lowercase letters (a-z)
'''

def string_compression(s: str):
    compressed_string: str = ""
    count_consecutive: int = 0

    for i in range(len(s)):
        count_consecutive += 1

        # if the next element is different from the previous one and end
        if ((i + 1) == len(s) or s[i] != s[i+1]):
            compressed_string += f"{s[i]}{count_consecutive}"
            count_consecutive = 0

    return compressed_string


if __name__ == "__main__":
    s = "aabcccccaa"
    print(string_compression(s)) # expected output: a2b1c5a2
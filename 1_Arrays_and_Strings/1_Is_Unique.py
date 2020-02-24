# Implement an algorithm to determine if a string has all unique characters
# What if you cannot use additional data structures

def is_unique(s):
    chars = []
    for char in s:
        if char in chars:
            return False
        else:
            chars.append(char)
    return True

print(is_unique("aaaaa"))
print(is_unique("asdf"))

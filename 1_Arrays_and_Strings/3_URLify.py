# Write a method to replace all spaces in a string with '%20'
# You may assume the string has sufficient space at the end to hold the additional chars,
# and that you are given the "true" length of the string

def urlify(s):
    return s.replace(" ", "%20")

print(urlify("asdfasdfasdf"))
print(urlify("asdf asdf asdf"))
print(urlify("asdf38g 339g"))

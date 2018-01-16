"""Given a string, find out if its characters can be rearranged to form a palindrome."""


def palindromeRearranging(inputString):
    dict_str = {}
    for letter in inputString:
        dict_str[letter] = inputString.count(letter)%2
    oddcount = 0
    values = dict_str.values()
    for v in values:
        oddcount += v
    if oddcount > 1:
        return False
    else:
        return True

inputString = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc"
# expected result = false
print(palindromeRearranging(inputString))

inputString = "tacoact"
#expected result = True
print(palindromeRearranging(inputString))
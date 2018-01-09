"""Check to see if a given string is a palindrome"""

def checkPalindrome(inputString):
    i = list(inputString)
    r = list(reversed(inputString))
    p = True
    for x in range(0,len(inputString)):
        if i[x] != r[x]:
            p = False
            break
    return p

# expected result = true
print(checkPalindrome("tacocat"))

# expected result = False
print(checkPalindrome("not a palindrome"))
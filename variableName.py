def variableName(name):

    import re
    legal = re.compile('[\w]+')
    digits = re.compile('[\d]')
    
#     fail if first character is a digit
    v1 = re.search(digits, name[0])
    if v1:
        return False
#     now make sure the length of the regex match is the same as the length of the original    
    v = re.search(legal, name)
    if len(name) == len(v.group(0)):
        return True
    else:
        return False
    
    
   

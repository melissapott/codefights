"""Given a year, return the century it is in"""

def centuryFromYear(year):
    century = int(year/100)+1
    mod = year%100
    if mod == 0:
        century = century -1
    pass
    return century

# expected output = 20
print(centuryFromYear(1905))
# expected output = 21
print(centuryFromYear(2017))
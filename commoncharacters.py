"""Given two strings, find the number of common characters between them."""

def commonCharacterCount(s1, s2):
	result = 0

	for item in s1:
		first_count = s1.count(item)
		second_count = s2.count(item)
		result += min(first_count,second_count)
		s1 = s1.replace(item, "")
		s2 = s2.replace(item, "")

	return result

s1 = "aabcc"
s2 = "adcaa"
# expected result = 3
print(commonCharacterCount(s1,s2))

s1 = "zzzz"
s2 = "zzzzzzzzz"
# expected result = 4
print(commonCharacterCount(s1,s2))
"""Given an array of strings, return another array containing all of its longest strings."""

def allLongestStrings(inputArray):
	output = []
	inputArray.sort(key=len, reverse=True)
	longest = len(inputArray[0])
	for item in inputArray:
		if len(item) == longest:
			output.append(item)

	return output

# expected result = ["aba", "vcd", "aba"]
inputArray = ["aba", "aa", "ad", "vcd", "aba"]
print(allLongestStrings(inputArray))

# expected result = ["eeee", "abcd"]
inputArray = ["abc", "eeee", "abcd", "dcd"]
print(allLongestStrings(inputArray))
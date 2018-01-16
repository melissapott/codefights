"""You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input."""

def arrayChange(inputArray):
	passCount = 0

	for i in range(1,len(inputArray)):
		if inputArray[i] <= inputArray[i-1]:
			diff = (inputArray[i-1] - inputArray[i] + 1)
			passCount += diff
			inputArray[i] += diff
	return passCount


inputArray = [-1000, 0, -2, 0]
# expected result = 5
print(arrayChange(inputArray))

"""Given an array of integers, find the maximal absolute difference between any two of its adjacent elements."""

def arrayMaximalAdjacentDifference(inputArray):
	differences = []
	for x in range(0,len(inputArray)-1):
		dif = max(inputArray[x], inputArray[x+1]) - min(inputArray[x],inputArray[x+1])
		differences.append(dif)
	return max(differences)

inputArray = [2, 4, 1, 0]
# expected output = 3
print(arrayMaximalAdjacentDifference(inputArray))

inputArray = [-1, 4, 10, 3, -2]
# expected output = 7
print(arrayMaximalAdjacentDifference(inputArray))

inputArray = [-7,5,9]
# expected output = 12
print(arrayMaximalAdjacentDifference(inputArray))
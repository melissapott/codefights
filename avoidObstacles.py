"""You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example

For inputArray = [5, 3, 6, 7, 9], the output should be
avoidObstacles(inputArray) = 4."""

def avoidObstacles(inputArray):
	results = []
	results.append(max(inputArray)+1)
	for x in range(2, max(inputArray)):
		results.append(x)
		for i in inputArray:
			if i % x == 0:
				results.remove(x)
				break
	return(min(results))

inputArray = [5,3,6,7,9]
# expected output 4
print(avoidObstacles(inputArray))

inputArray = [2,3]
# expected output = 4
print(avoidObstacles(inputArray))

inputArray = [1,4,10,6,2]
# expected output = 7
print(avoidObstacles(inputArray))
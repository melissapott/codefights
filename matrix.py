"""After they became famous, the CodeBots all decided to move to a new building and live together. The building is represented by a rectangular matrix of rooms. Each cell in the matrix contains an integer that represents the price of the room. Some rooms are free (their cost is 0), but that's probably because they are haunted, so all the bots are afraid of them. That is why any room that is free or is located anywhere below a free room in the same column is not considered suitable for the bots to live in.

Help the bots calculate the total price of all the rooms that are suitable for them."""

def matrixElementsSum(matrix):
	sum = 0
	for y in range(len(matrix[0])):
		for x in range(len(matrix)):
			if matrix[x][y] > 0:
				sum += matrix[x][y]
			else:
				break

	return sum

# expected result = 9
matrix = [[0,1,1,2],
 [0,5,0,0],
 [2,0,3,3]]
print(matrixElementsSum(matrix))

# expected result = 9
matrix = [[1,1,1,0],
 [0,5,0,1],
 [2,1,3,10]]
print(matrixElementsSum(matrix))
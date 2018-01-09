"""Given an array of integers, find the pair of adjacent elements that has the largest product and return that product."""


def adjacentElementsProduct(inputArray):
	products = []
	for x in range (0,len(inputArray)-1):
		products.append(inputArray[x]*inputArray[x+1])
	return max(products)

# expected result = 21
inputArray = [3, 6, -2, -5, 7, 3]
print(adjacentElementsProduct(inputArray))

#expected result = 6
inputArray = [5, 1, 2, 3, 1, 4]
print(adjacentElementsProduct(inputArray))

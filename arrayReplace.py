def arrayReplace(inputArray, elemToReplace, substitutionElem):
	for i in range(0,len(inputArray)):
		if inputArray[i] == elemToReplace:
			inputArray[i] = substitutionElem
	return inputArray

inputArray = [1,2,1]
elemToReplace = 1
substitutionElem = 3

print(arrayReplace(inputArray, elemToReplace, substitutionElem))
"""Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees.  Trees are represented as -1"""

def sortByHeight(a):
	heights = a.copy()
	heights.sort()

	for x in range(heights.count(-1)):
		heights.remove(-1)

	i = 0
	for x in range(len(a)):
		if a[x] != -1:
			a[x] = heights[i]
			i += 1
	return a


a= [-1, 150, 190, 170, -1, -1, 160, 180]
# expected output = [-1, 150, 160, 170, -1, -1, 180, 190]
print(sortByHeight(a))
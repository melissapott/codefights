"""The pixels in the input image are represented as integers. The algorithm distorts the input image in the following way: Every pixel x in the output image has a value equal to the average value of the pixel values from the 3 × 3 square that has its center at x, including x itself. All the pixels on the border of x are then removed.

Return the blurred image as an integer, with the fractions rounded down."""


def boxBlur(image):
	result = []
	width = len(image[0])
	depth = len(image)
	for i in range(0,depth-2):
		answer = []
		for j in range(0,width-2):
			answer.append(findAvg(i,j,image))
		result.append(answer)
	return(result)



def findAvg(x,y,box):
	total = 0
	for i in range(x,x+3):
		for j in range(y,y+3):
			total += box[i][j]
	return int(total/9)


image = [[1,1,1],[1,7,1],[1,1,1]]
# expected output = [[1]]
print(boxBlur(image))

image = [[0,18,9],[27,9,0],[81,63,45]]
# expected output = [[28]]
print(boxBlur(image))

image = [[7,4,0,1],[5,6,2,2],[6,10,7,8],[1,4,2,0]]
# expected output = [[5,4],[4,4]]
print(boxBlur(image))

def minesweeper(matrix):
	#determine height and width of matrix
	height = len(matrix)
	width = len(matrix[0])

	# build an empty board
	board = []
	for i in range(0,height):
		row = []
		for i in range(0,width):
			row.append(0)
		board.append(row)

	# look at each space to see if that space contains True in matrix
	for x in range(0,height):
		for y in range(0,width):
			if matrix[x][y] == True:
				# increment the boxes above unless we're already at the top
				if x > 0:
					if y-1 >= 0:
						board[x-1][y-1] += 1
					board[x-1][y] += 1
					if y+1 < width:
						board[x-1][y+1] += 1

				# increment the boxes to the left and right
				if y-1 >= 0:
					board[x][y-1] += 1
				if y+1 < width:
					board[x][y+1] += 1

				# increment the boxes below unless we're already at the bottom
				if x+1 < height:
					if y-1 >= 0:
						board[x+1][y-1] += 1
					board[x+1][y] += 1
					if y+1 < width:
						board[x+1][y+1] += 1

	return(board)








matrix = [[True,False,False],[False,True,False],[False,False,False]]
matrix = [[True,False,False,True],
 [False,False,True,False],
 [True,True,False,True]]

print(minesweeper(matrix))
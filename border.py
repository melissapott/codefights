"""Given a rectangular matrix of characters, add a border of asterisks(*) to it."""

def addBorder(picture):
	top = "*" * (len(picture[0]))
	picture.insert(0,top)
	picture.append(top)
	bordered = []
	for i in range(len(picture)):
		newline = '*' + picture[i] + '*'
		bordered.append(newline)

	return(bordered)



picture = ["abc",
           "ded"]

print(addBorder(picture))
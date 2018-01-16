"""Call two arms equally strong if the heaviest weights they each are able to lift are equal.

Call two people equally strong if their strongest arms are equally strong (the strongest arm can be both the right and the left), and so are their weakest arms.

Given your and your friend's arms' lifting capabilities find out if you two are equally strong."""

def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
	if yourLeft > yourRight:
		yourStrong = yourLeft
		yourWeak = yourRight
	else:
		yourStrong = yourRight
		yourWeak = yourLeft

	if friendsLeft > friendsRight:
		friendStrong = friendsLeft
		friendWeak = friendsRight
	else:
		friendStrong = friendsRight
		friendWeak = friendsLeft

	if yourStrong == friendStrong and yourWeak == friendWeak:
		return True
	else:
		return False

yourLeft = 15
yourRight = 10
friendsRight = 15
friendsLeft = 10
# expected output = true
print(areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight))

yourLeft = 15
yourRight = 10
friendsRight = 15
friendsLeft = 15
# expected output = false
print(areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight))
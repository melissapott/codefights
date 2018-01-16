"""Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar."""

def areSimilar(a,b):
	diffa = []
	diffb = []
	# check to see if they're equal initially
	if a == b:
		return True

	for i in range(len(a)):
		if len(diffa) <= 2:
			if a[i] != b[i]:
				diffa.append(a[i])
				diffb.append(b[i])
		else:
			return False
	diffb.reverse()
	if diffb == diffa:
		return True
	else:
		return False

a = [1,2,3]
b = [2,1,3]
# expected result = true

print(areSimilar(a,b))
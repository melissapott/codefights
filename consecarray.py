"""Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed."""


def makeArrayConsecutive2(statues):
	statues = sorted(statues)
	missing = 0
	for x in range(1,len(statues)):
		diff = (statues[x] - statues[x-1])
		if diff > 1:
			missing = missing + diff-1
	return missing

# expected result = 3
statues = [6,2,3,8]
print(makeArrayConsecutive2(statues))

# expected result = 0
statues = [4,5,6]
print(makeArrayConsecutive2(statues))
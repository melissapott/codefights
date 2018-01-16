"""Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not."""

def isLucky(n):
	first = second = 0
	ticket = str(n)
	for x in range(len(ticket)):
		if x < len(ticket)/2:
			first += int(ticket[x])
		else:
			second += int(ticket[x])
			if second > first:
				return False

	if first == second:
		return True
	else:
		return False

n = 1230
# expected result = true
print(isLucky(n))

n = 239017
# expected result = False
print(isLucky(n))
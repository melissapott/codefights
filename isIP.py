"""An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

IPv4 addresses are represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255 inclusive, separated by dots, e.g., 172.16.254.1.

Given a string, find out if it satisfies the IPv4 address naming rules."""

def isIPv4Address(inputString):
	splitStr = inputString.split('.')
	if len(splitStr) != 4:
		return False
	for x in range (0,4):
		for char in splitStr[x]:
			if char.isalpha():
				return False
		if splitStr[x] == "" or int(splitStr[x]) < 0 or int(splitStr[x]) > 255:
			return False
	return True

inputString = ".254.255.0"
# expected output = False
print(isIPv4Address(inputString))

inputString = "xyz.0.0.1"
# expected output = False
print(isIPv4Address(inputString))

inputString = "255.255.255.0"
# expected output = True
print(isIPv4Address(inputString))
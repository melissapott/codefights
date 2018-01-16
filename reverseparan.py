"""You have a string s that consists of English letters, punctuation marks, whitespace characters, and brackets. It is guaranteed that the parentheses in s form a regular bracket sequence.

Your task is to reverse the strings contained in each pair of matching parentheses, starting from the innermost pair. The results string should not contain any parentheses."""

def reverseParentheses(s):

	count = s.count('(')
	for x in range(count):
		# find the inside open paren
		left_index = s.rfind('(')
		left = s[:left_index:]
		right_index = s.find(')',left_index)
		right = s[right_index+1::]
		inside = s[right_index-1:left_index:-1]
		s = left + inside + right

	return(s)

s = "a(bc)de"
# expected output = "acbde"
print(reverseParentheses(s))

s = "a(bcdefghijkl(mno)p)q"
# expected output = "apmnolkjihgfedcbq"
print(reverseParentheses(s))
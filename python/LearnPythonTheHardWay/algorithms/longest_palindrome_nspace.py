############################################################
#
#  longest_palindrome_nspaces.py
#
# this program will show you how to get the longest palindrome with only n spaces.
#
############################################################


"""
optimize the longest_palindrome algorithm with less spaces.

"""

def initialize(s, n):
	m = [[1, 0] for i in range(n)]
	for i in range(n-1):
		if s[i] == s[i+1]:
			m[i][1] = 2
	print(m)
	return m

def longestPalindrom(s):
	length = len(s)
	m = initialize(s, length)
	start = end = -1
	longest = -1
	for i in range(2, length):
		for j in range(0, length - i):
			print ("m[j+1][(i)%2]={0}".format(m[j+1][(i)%2]))
			if s[j] == s[i + j] and m[j+1][(i)%2] == i - 1:
				m[j][(i+1)%2] = i
				print ("in step {0}, j = {1}, m[j+i]={2}, m[j]={3}".format(i, j, m[j+1][i%2], m[j][(i+1)%2]))
				if m[j] > longest:
					longest = m[j][(i+1)%2]
					start = j
					end = i + j
	print("Longest palindrome = {0}, start = {1}, length = {2}".format(s[start : end], start, longest))


longestPalindrom("ajhabcdcbahh")
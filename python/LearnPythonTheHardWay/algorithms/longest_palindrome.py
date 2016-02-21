############################################################
#
#  longest_palindrome.py
#
# this program is to demonstrate the algorithm to find the longest palindrome 
#
############################################################


"""

p[i,j] = k where k is the longest palindrome
p[i-1,j+1] = K + 2 if s[i-1] == s[j+1]

and the initial condition is 

p[i, i] = 1
p[i, i + 1] = 2 if s[i] == s[j]

"""


def initialize(s, n):
	m = [[0 for j in range(n)] for i in range(n)]
	for i in range(n):
		m[i][i] = 1
	for i in range(n - 1):
		m[i][i+1] = 2 if s[i] == s[i+1] else 0
	return m

def printAux(m, n):
	for i in range(n):
		for j in range(i, n):
			print ("{0},{1}: {2}".format(i, j, m[i][j]))

def longestPalindrom(s):
	length = len(s)
	p = initialize(s, length)
	#for k in range(2, length):
	#	for i in range(length):
	#		for j in range(i+k,length):
	#			if p[i+1][j-1] != 0 and s[i] == s[j]:
	#				p[i][j] = p[i+1][j-1]  + 2
	for k in range(2, length):
		for i in range(length - k):
			j = k + i
			if s[i] == s[j] and p[i+1][j-1] != 0:
				#print("{},{} ".format(i, j))
				p[i][j] = p[i+1][j-1] + 2
	longest = 0
	start = -1;
	end = -1;
	for i in range(length):
		for j in range(i, length):
			if p[i][j] > longest:
				longest = p[i][j]
				start = i
				end = j
	if longest != 0:
		print("Longest string is {}, start = {}, end = {}".format(str(longest), start, end))


#longestPalindrom("aaa")
longestPalindrom("ajhabcdcbahh")
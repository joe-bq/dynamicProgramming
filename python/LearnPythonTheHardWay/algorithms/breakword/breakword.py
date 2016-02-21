class Solution(object):
	def __init__(self):
		pass
	def word_break(self, s, dict):
		roots = set()
		for word in dict:
			if word in s:
				roots.add(word)
		return self.word_break_filtered(s, roots)
		# do not call this way 
		#return word_break_filtered(self, s, roots)
	def word_break_filtered(self, s, roots):
		if s == "":
			return True
		for word in roots:
			if s.startswith(word):
				if self.word_break_filtered(s[len(word):], roots):
					return True
		return False

if __name__ == "__main__":
	solution = Solution()
	result = solution.word_break("leetcode", set(["leet", 'code']))
	print "can leetcode be breaken up with [leet, code] ", result
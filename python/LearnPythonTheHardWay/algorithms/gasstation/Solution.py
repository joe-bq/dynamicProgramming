class Solution(object):
	def __init__(self):
		pass
	def canCompleteCircuit(self, gas, cost):
		length = len(gas)
		howfar = list()
		for i in range(length):
			howfar[i] = gas[i] - cost[i]
		for i in range(length):
			for j in range(1, length):
				if howfar[i] < 0: 
					break
				next = (i + j) % length
				howfar[i] += gas[next] - cost[next]

			if howfar[i] >= 0:
				return i
		return -1

if __name__ == "__main__":
	solution = Solution()
	gas = list([4, 8, 25, 6, 10])
	cost = list([5, 10, 20, 6, 7])
	station = solution.canCompleteCircuit(gas, cost)
	if station != -1:
		print "Can work out the solution " + station
	else:
		print 'Cannot work out the solution'

=begin
file
	BinaryTreePaths.rb
description
	print all the paths from root to leaves
ref:
   https://leetcode.com/problems/binary-tree-paths/
=end


class TreeNode
	attr_accessor :val, :left, :right
	def initialize(x)
		@val = x
		@left = nil
		@right  = nil
	end
end

class Solution
	def initialize
		@crumbs = []
	end

	public
	def binaryTreePaths(root)
		result = []
		binaryTreePathWalker(root, result)
		result
	end

	private 
	def crumbsToString(crumbs)
		crumbs.select { |x| x.to_s}.join("->")
	end

	def binaryTreePathWalker(root, result)
		if not root.nil?
			@crumbs << root.val
			if root.left.nil? and root.right.nil?
				result << crumbsToString(@crumbs)
			end

			if not root.left.nil?
				binaryTreePathWalker(root.left, result)
			end

			if not root.right.nil?
				binaryTreePathWalker(root.right, result)
			end

			@crumbs.pop()
		end
	end
end

def binary_tree_paths(root)
	solution = Solution.new
	solution.binaryTreePaths(root)
end
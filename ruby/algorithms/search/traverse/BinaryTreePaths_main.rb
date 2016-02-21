=begin
file
	BinaryTreePaths_main.rb
description
	the main function to test harness the BinaryTreePaths
ref:
   https://leetcode.com/problems/binary-tree-paths/
=end


require 'BinaryTreePaths.rb'

root = TreeNode.new(1)
root.left = TreeNode.new(2)
root.right = TreeNode.new(3)
root.left.right = TreeNode.new(5)

# solution = Solution.new
# res = solution.binaryTreePaths(root)

res = binary_tree_paths(root)
puts res
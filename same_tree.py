
#It might help to start with these two classes


#Binary tree node definition
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def same_tree(self, p, q):
		'''
		type p: TreeNode
		type q: TreeNode

		'''
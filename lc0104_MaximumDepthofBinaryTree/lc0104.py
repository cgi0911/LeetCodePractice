# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    global_max = 0
    def traverse(self, root, curr_depth):
        self.global_max = max(curr_depth, self.global_max)
        
        if (root.left): self.traverse(root.left, curr_depth + 1)
        if (root.right): self.traverse(root.right, curr_depth + 1)
        
        
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root == None):  return 0
        self.traverse(root, 1)  # Root is at depth 1
        return self.global_max
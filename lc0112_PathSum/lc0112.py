# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _hasPathSum(self, root, target, partial):
        if (root.left == None and root.right == None):
            # Root is a leaf. Check if path sum equal to target.
            if (partial + root.val == target):
                return True
            else:
                return False
        
        if (root.left):
            if (self._hasPathSum(root.left, target, partial+root.val)):
                return True
        if (root.right):
            if (self._hasPathSum(root.right, target, partial+root.val)):
                return True
        
        return False
        
        
    def hasPathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # Do a DFS to check each root-to-leaf path's path sum.
        # Any True will result in a return True from upper layer.
        if (root == None):
            return False
        
        return self._hasPathSum(root, target, 0)
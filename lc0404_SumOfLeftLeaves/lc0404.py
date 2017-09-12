# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _sumOfLeftLeaves(self, root):
        ret = 0
        
        # First check if left child is a leaf
        if (root.left != None):
            if (root.left.left == None and root.left.right == None):
                # root.left is a leaf. Add its value.
                ret += root.left.val
            else:
                # Recursively search for left leaves under root.left
                ret += self._sumOfLeftLeaves(root.left)
        
        if (root.right != None):
            # Recursively search for left leaves under root.right
            ret += self._sumOfLeftLeaves(root.right)
            
        return ret
    
    
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root == None):
            return 0
        
        return self._sumOfLeftLeaves(root)
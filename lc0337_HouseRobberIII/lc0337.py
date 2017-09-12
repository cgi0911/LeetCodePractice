# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _rob(self, root, robroot, rob_map):
        """
        :type root: TreeNode
        :type robroot: bool
        :rtype: int
        """
        if ((root, robroot) in rob_map):
            return rob_map[(root, robroot)]
        
        ret = 0
        
        if (robroot):
            ret = root.val
            if (root.left):     ret += self._rob(root.left,  False, rob_map)
            if (root.right):    ret += self._rob(root.right, False, rob_map)
        else:
            if (root.left):     ret += max(self._rob(root.left,  True, rob_map),
                                           self._rob(root.left,  False, rob_map))
            if (root.right):    ret += max(self._rob(root.right, True, rob_map),
                                           self._rob(root.right, False, rob_map))
        
        rob_map[(root, robroot)] = ret     # Memorization for future use
        return ret
        
        
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root == None):
            return 0
        
        rob_map = {}
        
        return max(self._rob(root, True, rob_map),
                   self._rob(root, False, rob_map))
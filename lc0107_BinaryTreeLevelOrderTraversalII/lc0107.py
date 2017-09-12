# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        levels = []     # list of levels -> list of nodes
        curr_level = []
        
        if (root == None):
            return ret
        
        curr_level.append(root)
        
        while (len(curr_level) != 0):
            levels.append(curr_level)
            next_level = []
            
            for node in curr_level:
                if (node.left):     next_level.append(node.left)
                if (node.right):    next_level.append(node.right)
            
            curr_level = next_level
            
        for i in reversed(range(len(levels))):
            curr_level = levels[i]
            ret.append([])
            
            for node in curr_level:
                ret[-1].append(node.val)
                
        return ret
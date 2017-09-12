# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _binaryTreePaths(self, root, res, partial):
        """
        :type root: TreeNode
        :type res: List[str]
        :type partial: str
        """
        # root: root node of traversal
        # res: reference to a list of strings that stores results
        # partial: partial string (path) before it reaches leaf
        if (root.left == None and root.right == None):
            res.append(partial + str(root.val))
        
        if (root.left):
            self._binaryTreePaths(root.left, res, partial + str(root.val) + "->")
        if (root.right):
            self._binaryTreePaths(root.right, res, partial + str(root.val) + "->")
            
        
    
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ret = []
        
        if (root == None):
            return ret
        
        self._binaryTreePaths(root, ret, "")
        
        return ret
    

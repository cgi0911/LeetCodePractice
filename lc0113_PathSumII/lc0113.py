# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _pathSum(self, root, target, partial_path, partial_sum, res):
        """
        :type root: TreeNode
        :type target: int
        :type partial_path: List(int)
        :type partial_sum: int
        """
        if (root.left == None and root.right == None):
            if (partial_sum + root.val == target):
                res.append(partial_path + [root.val])
            return  # Leaf will trigger a return
        
        if (root.left):
            # Explore left subtree
            self._pathSum(root.left, target, partial_path + [root.val],
                          partial_sum + root.val, res)
        if (root.right):
            # Explore left subtree
            self._pathSum(root.right, target, partial_path + [root.val],
                          partial_sum + root.val, res)
    
    
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []    # List to store the results
        
        if (root == None):
            return res
        
        self._pathSum(root, target, [], 0, res)
        
        return res
        
        
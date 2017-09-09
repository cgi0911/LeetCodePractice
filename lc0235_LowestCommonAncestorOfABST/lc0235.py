# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if (p.val > q.val):
            p, q = q, p     # Swap to ensure p < q
        
        if (p.val <= root.val <= q.val):
            # Equal for the case where one is the ancestor of the other, or the two nodes overlap
            return root
        
        else:
            if (p.val <= root.val):
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                return self.lowestCommonAncestor(root.right, p, q)
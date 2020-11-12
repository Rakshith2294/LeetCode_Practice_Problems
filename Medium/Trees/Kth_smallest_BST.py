# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(node,res):
            if not node:
                return
            inorder(node.left,res)
            res.append(node.val)
            inorder(node.right,res)
            return res
        res = []
        val = inorder(root,res)
        return val[k-1]

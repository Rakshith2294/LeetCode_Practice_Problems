# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        def inorder(node,res):
            if not node:
                return
            inorder(node.left,res)
            res.append(node.val)
            inorder(node.right,res)
            return res

        res = list()
        return inorder(root,res)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def postorder(node,res):
            if not node:
                return
            postorder(node.left,res)
            postorder(node.right,res)
            res.append(node.val)

            return res
        res = []
        return postorder(root,res)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symm(l,r):
            if l is None and r is None:
                return True
            if l is None or r is None:
                return False

            if l.val!=r.val:
                return False

            return symm(l.left,r.right) and symm(l.right,r.left)




        if root is None:
            return True

        return symm(root.left,root.right)

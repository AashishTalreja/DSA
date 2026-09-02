# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result=[]
        curr=[root]
        next=[]

        l_r=True
        while curr:
            level=[]

            while curr:
                node=curr.pop()
                level.append(node.val)

                if l_r:
                    if node.left:
                        next.append(node.left)
                    if node.right:
                        next.append(node.right)

                else:
                    if node.right:
                        next.append(node.right)
                    if node.left:
                        next.append(node.left)
                
            result.append(level)
            curr,next=next,curr
            l_r=not l_r

        return result

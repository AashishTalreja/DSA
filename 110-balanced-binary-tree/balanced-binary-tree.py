# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        # left=self.isBalanced(root.left)
        # right=self.isBalanced(root.right)

        # if abs(left-right)>1:
        #     return False
        # else:
        #     return True
        # stack=[[root,1]]
        # while stack:
        #     node,depth=stack.pop()
        #     stack.append([node.left,depth+1])
        #     stack.append([node.right,depth+1])

        # if node.left.left and not node.right.right or not node.left.left and node.right.right:
        #     return False
        # else:
        #     return True

        def height(node):
            if node is None:
                return 0
            
            left=height(node.left)
            if left==-1:
                return -1
            
            right=height(node.right)
            if right==-1:
                return -1

            if abs(left-right)>1:
                return -1

            return 1+max(left,right)

        return height(root)!=-1

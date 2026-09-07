# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        stack=[root]
        gain={}
        msum=float("-inf")

        while stack:
            node=stack[-1]

            if node.left is not None and node.left not in gain:
                stack.append(node.left)
                continue

            if node.right is not None and node.right not in gain:
                stack.append(node.right)
                continue

            stack.pop()

            left=max(0,gain.get(node.left,0))
            right=max(0,gain.get(node.right,0))

            msum=max(msum,left+node.val+right)

            gain[node]=node.val+max(left,right)

        return msum
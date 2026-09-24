# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res=root.val
        def dfs(node):
            if not node: return 0

            lMax=dfs(node.left)
            rMax=dfs(node.right)

            lMax=max(lMax,0)
            rMax=max(rMax,0)

            self.res=max(self.res,node.val+lMax+rMax)

            return node.val+max(lMax,rMax)
        dfs(root)
        return self.res
















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

            #with splitting
            self.res=max(self.res,node.val+lMax+rMax)

            #without splitting
            return node.val+max(lMax,rMax)
        dfs(root)
        return self.res













class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res=float("-INF")

        def dfs(curr):
            if not curr: return 0
            
            l=dfs(curr.left)
            r=dfs(curr.right)
            l=max(0,l)
            r=max(0,r)

            self.res=max(self.res,curr.val+l+r)

            return curr.val+max(l,r)
        dfs(root)
        return self.res













class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res=float("-INF")
        def dfs(curr):
            if not curr: return 0
            l=dfs(curr.left)
            r=dfs(curr.right)
            #Ignore negative contributions because they decrease the path sum.
            l=max(0,l)
            r=max(0,r)
            self.res=max(self.res,curr.val+l+r)
            return curr.val+max(l,r)
        dfs(root)
        return self.res
        



















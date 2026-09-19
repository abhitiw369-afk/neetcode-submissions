# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res=0 #class variable or global variable
        def dfs(curr):
            if not curr:
                return 0

            l=dfs(curr.left)
            r=dfs(curr.right)

            self.res=max(self.res,l+r) #updating each nodes' diameter
            return 1+max(l,r) #updating each nodes' max ht which we use in diameter        

        dfs(root)
        return self.res
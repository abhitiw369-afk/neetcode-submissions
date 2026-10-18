# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node,maxVal):
            if not node: return 0

            res=1 if node.val>=maxVal else 0
            maxVal=max(maxVal,node.val)
            res+=dfs(node.left,maxVal)
            res+=dfs(node.right,maxVal)
            return res

        return dfs(root,root.val)










class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count=0
        maxVal=float("-INF")
        def dfs(curr,maxVal):
            if not curr: return
            if curr.val>=maxVal: self.count+=1
            maxVal=max(maxVal,curr.val)
            dfs(curr.left,maxVal)
            dfs(curr.right,maxVal)
        dfs(root,maxVal)
        return self.count


















# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count=0
        self.ans=None

        def dfsI(node):
            if not node: return

            dfsI(node.left)
            self.count+=1
            if self.count==k:
                self.ans=node.val
                return

            dfsI(node.right)
            # return self.ans
        dfsI(root)

        return self.ans













class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans=0
        self.count=0
        def dfs(curr):
            if not curr: return

            dfs(curr.left)
            self.count+=1
            if self.count==k:
                self.ans=curr.val
            dfs(curr.right)
        dfs(root)
        return self.ans



















        
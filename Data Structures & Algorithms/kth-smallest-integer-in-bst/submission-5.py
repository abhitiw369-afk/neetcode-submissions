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

        def dfsI(node,k):
            if not node: return

            dfsI(node.left,k)
            self.count+=1
            if self.count==k:
                self.ans=node.val
                return

            dfsI(node.right,k)
            return self.ans
        dfsI(root,k)

        return self.ans
        
        
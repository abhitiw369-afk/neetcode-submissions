# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not s: return False
        if s and not t: return True

        if self.sameTree(s,t):
            return True

        return (self.isSubtree(s.left,t) or self.isSubtree(s.right,t))

    def sameTree(self,s,t):
        if not s and not t: return True
        if ((not s or not t) or (s.val!=t.val)): return False
        l=self.sameTree(s.left,t.left)
        r=self.sameTree(s.right,t.right)
        return (l and r)






class Solution:   
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not s and not t: return True
        if s and not t: return True
        if not s and t: return False

        def sameTree(s,t):
            if not s and not t: return True
            if ((not s or not t) or s.val!=t.val): return False

            l=sameTree(s.left,t.left)
            r=sameTree(s.right,t.right)

            return (l and r and s.val==t.val)

        if sameTree(s,t): return True

        return(self.isSubtree(s.left,t) or
        self.isSubtree(s.right,t))

        













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

        return (self.isSubtree(s.left,t) or self.isSubtree(s.right,t)) #short circuiting
        #returns T even one value is True and don't check other
        
    def sameTree(self,s,t):
        if not s and not t: return True
        if ((not s or not t) or (s.val!=t.val)): return False
        l=self.sameTree(s.left,t.left)
        r=self.sameTree(s.right,t.right)
        return (l and r)






class Solution:   
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        

        def sameTree(s,t): #while using inner helper fxn, we've to define it first before calling
            if not s and not t: return True
            if ((not s or not t) or s.val!=t.val): return False

            l=sameTree(s.left,t.left)
            r=sameTree(s.right,t.right)

            return (l and r and s.val==t.val)
        
        #for isSubtree, now.
        #execution will start from here

        if not s and not t: return True
        if s and not t: return True
        if not s and t: return False

        if sameTree(s,t): return True

        return(self.isSubtree(s.left,t) or
        self.isSubtree(s.right,t))

        



class Solution:   
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:

        def isSameTree(s,t):
            if not s and not t : return True
            if not s or not t: return False
            if s.val!=t.val: return False

            l=isSameTree(s.left,t.left)
            r=isSameTree(s.right,t.right)

            return (l and r)

        if not s and not t: return True
        if s and not t: return True
        if not s and t: return False

        if isSameTree(s,t): return True

        l=self.isSubtree(s.left,t)
        r=self.isSubtree(s.right,t)

        return (l or r)

        





class Solution:   
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:

        def isSameTree(s,t):
            if not s and not t: return True
            if not s or not t: return False
            if s.val!=t.val: return False

            l=isSameTree(s.left,t.left)
            r=isSameTree(s.right,t.right)

            return (l and r)




        if s and not t: return True
        if not s and t: return False
        if not s and not t: return True

        if isSameTree(s,t): return True

        l=self.isSubtree(s.left,t)
        r=self.isSubtree(s.right,t)

        return (l or r)


















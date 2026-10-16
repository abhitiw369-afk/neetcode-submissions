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
            #bcz diameter is max ht of lf subtree+max ht of right subtree so we needed max ht 
            #for each node       

        dfs(root)
        return self.res










class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res=0

        

        def dfs(curr):
            if not curr:
                return 0
            
            l=dfs(curr.left)
            r=dfs(curr.right)

            self.res=max(self.res,l+r)
            return 1+max(l,r)
        dfs(root)
        return self.res








class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #dfs as helper fxn bcz we want to ret height in terms to achieve diameter
        #but in ques we've only diameter to return, so another dfs is required as helper fxn

        self.res=0 #global fxn

        def dfs(curr):
            if not curr: return 0
            l=dfs(curr.left)
            r=dfs(curr.right)
            
            self.res=max(self.res,l+r)
            #res is written before return, bcz anything after return will never get executed
            return 1+max(l,r)
            

        dfs(root)
        return self.res













        









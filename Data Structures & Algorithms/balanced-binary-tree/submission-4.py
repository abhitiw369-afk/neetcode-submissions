# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(curr):
            if not curr: 
                return [True,0] #[0,1] 0 is T/F and 1 is the height
            
            #applying dfs to (B2T) to optimize
            l=dfs(curr.left)
            r=dfs(curr.right)

            if(l[0] and r[0] and abs(l[1]-r[1])<=1):
                balanced=True
            else:
                balanced=False
            return [balanced,1+max(l[1],r[1])] #return T/F and ht of each node to that particular node
        dfs(root)
        return dfs(root)[0] #as root is any node we've to return T/F
        
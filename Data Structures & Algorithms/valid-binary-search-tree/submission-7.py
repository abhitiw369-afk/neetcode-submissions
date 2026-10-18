# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node,lowLimit,upLimit):
            if not node: return True
            if not(lowLimit<node.val<upLimit):return False
            
            #whenever we recursively go to any node, we update left and right limits
            l=valid(node.left,lowLimit,node.val)
            r=valid(node.right,node.val,upLimit)

            return(l and r)
        
        return valid(root,float("-inf"),float("inf"))
        







class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr,LR,UP):
            if not curr: return True

            if not (LR<curr.val<UP): return False
            l=dfs(curr.left,LR,curr.val)
            r=dfs(curr.right,curr.val,UP)

            return (l and r)

        return dfs(root,float("-INF"),float("INF"))




















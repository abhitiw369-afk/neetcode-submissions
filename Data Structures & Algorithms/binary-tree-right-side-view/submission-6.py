# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        q=collections.deque()
        q.append(root)

        while q:
            node=None
            rs=None
            for _ in range(len(q)):
                node=q.popleft()
                if node:
                    rs=node#updates rightside of q in a single iteration
                    q.append(node.left)
                    q.append(node.right)
            if rs:
                res.append(rs.val)
        return res

        

















class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q=collections.deque()
        res=[]
        q.append(root)
        while q:
            rs=None
            node=None
            for _ in range(len(q)):#if 2 node are present initially, and their children are added,
                    #but loop only run the no. of time=no of nodes initially, not for added nodes. 
                node=q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            rs=node
            res.append(rs.val)
        return res




















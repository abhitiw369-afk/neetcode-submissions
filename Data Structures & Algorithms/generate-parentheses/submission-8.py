
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, curr = [], []

        def dfs(C, O):
            if C == O == n:
                res.append("".join(curr))
                return

            if C > O:
                curr.append(")")
                dfs(C, O+1)
                curr.pop()

            if C < n:
                curr.append("(")
                dfs(C+1, O)
                curr.pop()

        dfs(0, 0)
        return res







class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        curr=[]
        def dfs(O,C):
            if O==C==n:
                res.append("".join(curr))
                return
            if O<n:
                curr.append("(")
                dfs(O+1,C)
                curr.pop()
            if O>C:
                curr.append(")")
                dfs(O,C+1)
                curr.pop()
        dfs(0,0)
        return res





























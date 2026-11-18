class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        curr=[]

        def backtrack():

            #base case
            if len(curr)==len(nums):
                res.append(curr.copy())
                return
            
            #explore all numbers
            for n in nums:
                if n not in curr:

                    #choose
                    curr.append(n)

                    #explore
                    backtrack()

                    #backtrack/undo
                    curr.pop()
        backtrack()
        return res



class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def dfs(i,curr):
            if len(curr)==len(nums):
                res.append(curr.copy())
                return
            for n in nums:
                if n not in curr:
                    curr.append(n)
                    dfs(i+1,curr)

                    curr.pop()
                    
        dfs(0,[])
        return res



















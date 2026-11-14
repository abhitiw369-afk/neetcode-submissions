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

            
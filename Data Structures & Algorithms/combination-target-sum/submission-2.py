class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]

        def dfs(i,curr,total):
            if total==target: 
                res.append(curr.copy())
                return
            if total>target or i>=len(nums):return
            
            # Include
            curr.append(nums[i])
            dfs(i,curr,nums[i]+total)

             # Backtrack
            curr.pop()

            # Exclude
            dfs(i+1,curr,total)
        
        dfs(0,[],0)
        return res
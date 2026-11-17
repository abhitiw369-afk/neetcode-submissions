class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()

        def dfs(i,curr,total):
            if total==target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total>target:
                return
            
            #inlcude
            curr.append(candidates[i])
            dfs(i+1,curr,candidates[i]+total)

            #backtrack
            curr.pop()

            #exclude
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,curr,total)
        
        dfs(0,[],0)
        return res



class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        def dfs(i,curr,total):
            if total==target:
                res.append(curr.copy())
                return
            if i>=len(nums) or total>target:
                return
            curr.append(nums[i])
            dfs(i+1,curr,total+nums[i])
            total-nums[i]
            curr.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1,curr,total)
        dfs(0,[],0)
        return res






















        
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        def dfs(i):
            if i>=len(nums):
                res.append(subset.copy())
                return
            #to include
            subset.append(nums[i])
            dfs(i+1)

            #to not include
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res
        

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        curr=[]

        def dfs(i):
            if i == len(nums):
                res.append(curr.copy())
                return
            
            #include the curr number
            curr.append(nums[i])
            dfs(i+1)

            #backtrack=pop the last one
            curr.pop()

            #exclude the curr number
            dfs(i+1)
        dfs(0)
        return res




















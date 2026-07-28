class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = set()
        for k in range(len(nums)):
            i = k+1
            j = len(nums)-1
            while i < j :
                if nums[i]+nums[j]+nums[k] > 0 :
                    j -= 1
                elif nums[i]+nums[j]+nums[k] < 0 :
                    i += 1
                else :
                    arr.add((nums[k], nums[i], nums[j]))
                    i+=1
                    j-=1

                    

                    
        return [list(t) for t in arr] #list(t) converts every tuple into list in arr


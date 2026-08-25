# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        # arr = set()
        # for k in range(len(nums)):
        #     i = k+1
        #     j = len(nums)-1
        #     while i < j :
        #         if nums[i]+nums[j]+nums[k] > 0 :
        #             j -= 1
        #         elif nums[i]+nums[j]+nums[k] < 0 :
        #             i += 1
        #         else :
        #             arr.add((nums[k], nums[i], nums[j]))
        #             i+=1
        #             j-=1

                    

                    
        # return [list(t) for t in arr] #list(t) converts every tuple into list in arr

        # res = set()
        # nums.sort()
        # for k in range(len(nums)) :
        #     l = k+1
        #     r = len(nums)-1
            
        #     while l < r :
        #         sumnums = nums[k] + nums[l] + nums[r]

        #         if sumnums > 0 :
        #             r -= 1
        #         elif sumnums < 0 :
        #             l += 1
        #         else :
        #             res.add((nums[k] , nums[l] , nums[r]))
        #             l+=1
        #             r-=1
        # return [list(t) for t in res]




class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=set() #no duplicacy is demanded
        nums.sort()
        for k in range(len(nums)):
            l,r = k+1,len(nums)-1
            while l < r:
                sumnum=nums[l]+nums[r]+nums[k]

                if sumnum < 0:
                    l+=1
                elif sumnum > 0:
                    r-=1
                else:
                    res.add((nums[l],nums[r],nums[k]))
                    l+=1
                    r-=1
        return [list(t) for t in res]

        




















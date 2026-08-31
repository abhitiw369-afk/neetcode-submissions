# class Solution:
#     def findMin(self, nums: List[int]) -> int:
        #O(n) 
        # res = nums[0]

        # for n in nums:
        #     res = min(res, n)

        # return res

        #O(logn)
        # l,r = 0,len(nums)-1
        # res = float('inf')
        # while l <= r :

        #     if nums[l]<nums[r] : #for completely sorted array n rotated or no rotation
        #         res = min(res,nums[l])
        #         break
        #     m = (l+r)//2 #if rotated then
        #     res = min(res,nums[m])
        #     if nums[m]>=nums[l] :
        #         l = m+1
        #     else:
        #         r = m-1

        # return res
            

# class Solution:
#     def findMin(self, nums: List[int]) -> int:
        # res=float("inf")
        # for i in range(len(nums)):
        #     if nums[i]<res:
        #         res=nums[i]
        # return res


class Solution:
    def findMin(self, nums: List[int]) -> int:
        #if sorted without any rotation
        l,r=0,len(nums)-1
        res=float("inf")
        while l<=r:
            #for optimization,that if 1st ele is the sorted
            if nums[l]<nums[r]:
                res= min(nums[l],res)
                break
        
        #now,to tackle rotated array
            m=(l+r)//2
            if nums[m]>=nums[r]:
                l=m+1
            else:
                r=m-1
            res=min(res,nums[m])
        return res


#Non optimized solution
class Solution:
    def findMin(self, nums: List[int]) -> int:
        #if sorted without any rotation
        l,r=0,len(nums)-1
        res=float("inf")
        while l<=r:
        
        #now,to tackle rotated array as well as non rotated
            m=(l+r)//2
            if nums[m]>=nums[r]:
                l=m+1
            else:
                r=m-1
            res=min(res,nums[m])
        return res


        
















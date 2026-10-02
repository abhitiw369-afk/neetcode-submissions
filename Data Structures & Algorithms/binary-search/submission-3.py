# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
        
#         l,r=0,len(nums)-1

#         while l <= r :
#             m = (r+l)//2  #in py, there is no overflow
            
#             if nums[m] > target:
#                 r = m-1
#             elif nums[m] < target:
#                 l = m+1
#             else:
#                 return m
#         return -1






class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l <= r:
            m=(l+r)//2
            if nums[m]==target:
                return m
            elif nums[m]>target:
                r=m-1
            else:
                l=m+1
        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1

        while l<=r:
            mid=(l+r)//2
            if target<nums[mid]:
                r=mid-1
            elif target>nums[mid]:
                l=mid+1
            else:
                return mid
        return -1



















# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         #O(n)
#         # for p in range(len(nums)):
#         #     if target == nums[p] :
#         #         return p
#         # return -1
#         #O(logn)
#         l, r = 0, len(nums)-1

#         while l <= r :
#             m = (l+r)//2
#             if target == nums[m] :
#                 return m

#             if nums[m] >= nums[l] : #left sorted portion
#                 if target > nums[m] or target < nums[l] :
#                     l=m+1 #goto right
#                 else :
#                     r=m-1 #goto left
#             else : #right sorted portion
#                 if target < nums[m] or target > nums[r] :
#                     r=m-1
#                 else :
#                     l=m+1
#         return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
       
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1











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

#             if nums[m] >= nums[l] : #✅ To confirm that the left half [l...m] is sorted.
#                 if target > nums[m] or target < nums[l] :
#                     l=m+1 #goto right
#                 else :
#                     r=m-1 #goto left
#             else : #✅ To confirm that the right half [m+1...r] is sorted.
#                 if target < nums[m] or target > nums[r] :
#                     r=m-1
#                 else :
#                     l=m+1
#         return -1


# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
       
#         for i in range(len(nums)):
#             if nums[i]==target:
#                 return i
#         return -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l <= r:
            m=(l+r)//2
            if target==nums[m]:
                return m
            
            #check if left sub arrey is sorted
            if nums[l]<=nums[m]: #"=" bcz there can be a single element too, an edge case
                #now check if our target is in left of left sorted part
                # if target < nums[m] and target >= nums[l]:
                if nums[l]<=target<nums[m]:
                    r=m-1
                else: #check is our target is in right part of left sorted part,i.e right of m
                    l=m+1
            else:#now by adjusting pointers we will get sorted right part
                #now check if our target is in which part in right part
                if nums[m] < target <= nums[r]:
                    l=m+1
                else:
                    r=m-1
        return -1
                













# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # l, r = 0, len(numbers)-1
        # while l < r :
        #     if numbers[l] + numbers[r] > target :
        #         r -= 1
        #     elif numbers[l] + numbers[r] < target:
        #         l += 1
        #     else:
        #         return [l+1,r+1]

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
        # l = 0
        # r = len(nums)-1
        
        # while l < r :

        #     if nums[l] + nums[r] > target :
        #         r -= 1
        #     elif nums[l] + nums[r] < target :
        #         l += 1
        #     else :
        #         return [l+1,r+1] #1-indexed array is taken


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        l = 0
        r = len(nums)-1

        while l < r :
            add = nums[l] + nums[r]

            if add > target :
                r -= 1
            elif add < target :
                l += 1
            else :
                return [l+1,r+1]
        





































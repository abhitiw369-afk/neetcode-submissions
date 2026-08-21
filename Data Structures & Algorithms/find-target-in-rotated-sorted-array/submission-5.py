class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for p in range(len(nums)):
            if target == nums[p] :
                return p
        return -1

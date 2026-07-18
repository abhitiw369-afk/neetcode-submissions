class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevMap = {} #empty hashmap to check in O(1)
        
        for i , n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i] #it gives value(index) of diff(key)
            
            prevMap[n] = i #index is working as a value
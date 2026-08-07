class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # prevMap = {} #empty hashmap to check in O(1)
        
        # for i , n in enumerate(nums):
        #     diff = target - n
        #     if diff in prevMap:
        #         return [prevMap[diff], i] #it gives value(index) of diff(key)
            
        #     prevMap[n] = i #index is working as a value and n is working as key


        # hmap = {}
        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in hmap:
        #         return [hmap[diff],i]
        #     hmap[n] = i


        seen = {}
        for i,n in enumerate(nums) :
            dif = target - n
            if dif in seen :
                return [seen[dif],i]
            seen[n] = i
































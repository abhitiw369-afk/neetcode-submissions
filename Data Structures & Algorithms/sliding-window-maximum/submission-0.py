class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        maxnums = []

        for r in range(k-1, len(nums)) :
            numk = set()
            numk.update(nums[l:r+1])
            maxnums.append(max(numk))
            l+=1
        return maxnums

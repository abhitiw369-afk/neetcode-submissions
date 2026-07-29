class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l = 0
        r = len(heights)-1
        while l < r :
            ht = min(heights[l],heights[r])
            b = r - l
            area1 = ht * b
            if heights[l] < heights[r] :
                l += 1
            else :
                r -= 1
            area = max(area,area1)
        return area

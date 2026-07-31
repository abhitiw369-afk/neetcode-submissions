class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lmax = 0
        seen = set()
        l = 0
        for r in range(len(s)) :
            while s[r] in seen :  # it removes everything from the left until that duplicate is gone.
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            lmax = max(lmax,r-l+1)
        return lmax
        
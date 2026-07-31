class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        seen = {}
        for r in range(len(s)) :
            seen[s[r]] = 1 + seen.get(s[r], 0)
            while (r-l+1) - max(seen.values()) > k :
                seen[s[l]] -= 1
                l += 1
            longest = max(longest, r-l+1)
        return longest
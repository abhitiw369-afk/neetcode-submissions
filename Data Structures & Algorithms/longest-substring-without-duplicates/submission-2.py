class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # lmax = 0
        # seen = set()
        # l = 0
        # for r in range(len(s)) :
        #     while s[r] in seen :  # it removes everything from the left until that duplicate is gone.
        #         seen.remove(s[l])
        #         l+=1
        #     seen.add(s[r])
        #     lmax = max(lmax,r-l+1)
        # return lmax


        lenmax = 0
        l = 0
        hmap = {}

        for r in range(len(s)) :
            char = s[r]
            hmap[char] = 1 + hmap.get(char, 0)

            while char in hmap and hmap[char] > 1 :
                hmap[s[l]] -= 1
                l += 1
            
            length = r-l+1
            lenmax = max(lenmax,length)
        return lenmax




















        
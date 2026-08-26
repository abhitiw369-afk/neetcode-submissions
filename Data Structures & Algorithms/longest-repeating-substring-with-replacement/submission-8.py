# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
        # l = 0
        # longest = 0
        # seen = {}
        # for r in range(len(s)) :
        #     seen[s[r]] = 1 + seen.get(s[r], 0)
        #     while (r-l+1) - max(seen.values()) > k :
        #         seen[s[l]] -= 1
        #         l += 1
        #     longest = max(longest, r-l+1)
        # return longest

        # lenmax = 0
        # l = 0
        # hmap = {}

        # for r in range(len(s)) :
        #     hmap[s[r]] = 1 + hmap.get(s[r],0)
        #     while (r-l+1) - max(hmap.values()) > k :
                
        #         hmap[s[l]] -= 1
        #         l += 1

        #     lenmax = max(lenmax,r-l+1)
        # return lenmax




# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:

#         seen = {}
#         longest = 0
#         l = 0

#         for r in range(len(s)) :
#             seen[s[r]] = 1 + seen.get(s[r], 0)

#             while (r-l+1) - max(seen.values()) > k :
#                 seen[s[l]] -= 1
#                 l += 1
#             longest = max(longest,r-l+1)
#         return longest



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        lenmax=0
        seen={}
        l=0
        for r in range(len(s)):
            ch=s[r]
            seen[ch]=1+seen.get(ch,0)

            while (r-l+1)-max(seen.values())>k:
                seen[s[l]]-=1
                l+=1

            lenmax=max(lenmax,r-l+1)
        return lenmax



















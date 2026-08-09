# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
        # if len(s1) > len(s2):
        #     return False

        # seen1 = {}
        # for ch in s1:
        #     seen1[ch] = 1 + seen1.get(ch, 0)

        # need = len(s1)
        # seen2 = {}

        # for i in range(need):
        #     seen2[s2[i]] = 1 + seen2.get(s2[i], 0)

        # if seen1 == seen2:
        #     return True

        # for r in range(need, len(s2)):
        #     l = r - need

        #     seen2[s2[l]] -= 1
        #     if seen2[s2[l]] == 0:
        #         del seen2[s2[l]]

        #     seen2[s2[r]] = 1 + seen2.get(s2[r], 0)

        #     if seen1 == seen2:
        #         return True

        # return False

        #considering example 1
        # seen1 = {}

        # for ch1 in s1 :
        #     seen1[ch1] = 1 + seen1.get(ch1, 0)

        # l = 0
        # seen2 = {}
        # for r in range(len(s2)) :

        #     seen2[s2[r]] = 1 + seen2.get(s2[r],0)

        #     if r-l+1 > len(s1) :
        #         seen2[s2[l]] -= 1

        #         if seen2[s2[l]] == 0 : # we care a:0, as we're comparing directly dictionaries
        #             del seen2[s2[l]]
                
        #         l += 1

        #     if seen1 == seen2 :
        #         return True

        # return False




class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        seen1 = {}
        for s in s1 :
            seen1[s] = 1 + seen1.get(s,0)
        seen2 = {}
        l = 0
        for r in range(len(s2)) :

            seen2[s2[r]] = 1 + seen2.get(s2[r],0)

            while (r-l+1) > len(s1) :
                seen2[s2[l]] -= 1
                if seen2[s2[l]] == 0 :
                    del seen2[s2[l]]
                l += 1

            if seen1 == seen2 :
                return True
        return False

            




















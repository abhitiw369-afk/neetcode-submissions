class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "" : return ""

        countT, window = {}, {}

        for c in t :

            countT[c] = 1 + countT.get(c,0)

        res, reslen = [-1,-1], float("inf")

        need = len(countT) #for distinct chars in t

        l = 0
        have = 0
        for r in range(len(s)) :
            
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in countT and window[s[r]] == countT[s[r]] :
                #have counter only increase when the char freq in window exactly matches char freq in countT
                have += 1

            while have == need :
                if (r-l+1) < reslen :
                    reslen = r-l+1
                    res = [l,r]

                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]: 

                    have -= 1

                l += 1

        l, r = res #tuple unpacking

        return s[l:r+1] if reslen != float('inf') else ""




            




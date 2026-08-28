# class Solution:
#     def minWindow(self, s: str, t: str) -> str:

        # if t == "" : return ""

        # countT, window = {}, {}

        # for c in t :

        #     countT[c] = 1 + countT.get(c,0)

        # res, reslen = [-1,-1], float("inf")

        # need = len(countT) #for distinct chars in t

        # l = 0
        # have = 0
        # for r in range(len(s)) :
            
        #     window[s[r]] = 1 + window.get(s[r], 0)

        #     if s[r] in countT and window[s[r]] == countT[s[r]] :
        #         #have counter only increase when the char freq in window exactly matches char freq in countT
        #         have += 1

        #     while have == need :
        #         if (r-l+1) < reslen :
        #             reslen = r-l+1
        #             res = [l,r]

        #         window[s[l]] -= 1

        #         if s[l] in countT and window[s[l]] < countT[s[l]]: 

        #             have -= 1

        #         l += 1

        # l, r = res #tuple unpacking

        # return s[l:r+1] if reslen != float('inf') else ""


        # if t == "": return ""
            

        # seen1 = {}
        # for ch in t:
        #     seen1[ch] = 1 + seen1.get(ch, 0)

        # seen2 = {}
        # l = 0

        # minLen = float("inf")
        # resL = 0

        # for r in range(len(s)):
        #     seen2[s[r]] = 1 + seen2.get(s[r], 0)

        #     while all(seen2.get(ch, 0) >= seen1[ch] for ch in seen1):

        #         if (r - l + 1) < minLen:
        #             minLen = r - l + 1
        #             resL = l

        #         seen2[s[l]] -= 1
        #         l += 1

        # return s[resL:resL + minLen] if minLen != float("inf") else ""

        # if t == "" : return ""
        # seen1 = {}
        # for ch in t :
        #     seen1[ch] = 1 + seen1.get(ch, 0) 

        # seen2 = {}
        # l= 0
        # lenmin = float("inf")
        # initL = 0
        # for r in range(len(s)) :
        #     seen2[s[r]] = 1 + seen2.get(s[r], 0) 

        #     while all(seen2.get(char, 0)>=seen1[char] for char in seen1 ): #fking imp
        #         if lenmin > (r-l+1):
        #             lenmin = r-l+1
        #             initL = l
                
        #         seen2[s[l]] -= 1
        #         l += 1

        # return s[initL:initL+lenmin] if lenmin != float("inf") else ""










# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if t == "" : return ""
#         seen1 = {}
#         for ch in t :
#             seen1[ch] = 1 + seen1.get(ch, 0) 

#         seen2 = {}
#         l= 0
#         lenmin = float("inf")
#         initL = 0
#         for r in range(len(s)) :
#             seen2[s[r]] = 1 + seen2.get(s[r], 0) 

#             while all(seen2.get(char, 0)>=seen1[char] for char in seen1 ): #fking imp
#                 if lenmin > (r-l+1):
#                     lenmin = r-l+1
#                     initL = l
                
#                 seen2[s[l]] -= 1
#                 l += 1

#         return s[initL:initL+lenmin] if lenmin != float("inf") else ""


#below is optimal solution, the one above is non optimal

                

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if t == "": return ""

#         countT={}
#         window={}
#         lenmin=float("inf")
#         l=0
#         res=[-1,-1]
#         for c in t:
#             countT[c]=1+countT.get(c,0)

#         have, need=0,len(countT) #have counts how many unique characters have reached their required frequency.       
#         for r in range(len(s)):
#             window[s[r]]=1+window.get(s[r],0)

#             if s[r] in countT and window[s[r]]==countT[s[r]]:
#                 have+=1

#             while have==need:
#                 if (r-l+1)<lenmin:
                    
                
#                     res=[l,r]
#                     lenmin=(r-l+1)

#                 window[s[l]]-=1
#                 if s[l] in countT and window[s[l]]<countT[s[l]]:
#                     have-=1
#                 l+=1

#         l,r =res #unpacking

#         return s[l:r+1] if lenmin!=float("inf") else ""




# class Solution:
#     def minWindow(self, s: str, t: str) -> str:

#         if t=="" : return ""

#         countT={}
#         for c in t:
#             countT[c]=1+countT.get(c,0)
#         window={}
#         res=[-1,-1]
#         lenmin=float("inf")
#         have,need=0,len(countT)

#         l=0
#         for r in range(len(s)):
#             window[s[r]]=1+window.get(s[r],0)

#             if s[r] in countT and window[s[r]]==countT[s[r]]:
#                 have+=1

#             while have==need:
#                 if lenmin>(r-l+1):
#                     lenmin=(r-l+1)
#                     res=[l,r]

#                 window[s[l]]-=1
                

#                 if s[l] in countT and window[s[l]]<countT[s[l]]:
#                     have-=1
#                 l+=1

#         l,r=res

#         return s[l:r+1] if lenmin!=float("inf") else ""

        
        
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":return ""

        countT={}
        for c in t:
            countT[c]=1+countT.get(c,0)

        window={}
        l=0
        res=[-1,-1]
        lenmin=float("inf")
        have,need=0,len(countT)

        for r in range(len(s)):
            window[s[r]]=1+window.get(s[r],0)

            if s[r] in countT and countT[s[r]]==window[s[r]]:
                have+=1
            
            while have==need:
                if lenmin>(r-l+1):

                    lenmin=(r-l+1)
                    res=[l,r]
                window[s[l]]-=1
                
                
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if lenmin!=float("inf") else ""


        

















            




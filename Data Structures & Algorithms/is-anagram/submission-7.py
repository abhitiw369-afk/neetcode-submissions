# class Solution():

#     def isAnagram(self, s : str, t : str  ) -> bool:

#         # if len(s) != len(t):
#         #     return False
#         # S, T = {}, {}  #empty dictionaries are created

#         # for i in range(len(s)): #makes key - value pair for both dictionaries
#         #     S[s[i]] =1+ S.get(s[i],0)
#         #     T[t[i]] =1+ T.get(t[i],0)

#         # for c in S:
#         #     if S[c] != T.get(c,0): #checks if for same char both dict has same value
#         #         return False
        
#         # return True

#         if len(s) != len(t) :
#             return False

#         S, T = {}, {}

#     #to store each character as key and thier frequency as value
#         for i in range(len(s)):
#             S[s[i]] = 1 + S.get(s[i],0) #if set has s[i], return value, else 0
#             T[t[i]] = 1 + T.get(t[i],0)
#         #stored every character with thier respective frequency

#         #now we've to compare frequencies
#         for c in S:
#             if S[c] != T.get(c,0): #every character's freq in S if not same as every char freq in T
#                 return False
#         return True

# class Solution():

#     def isAnagram(self, s : str, t : str  ) -> bool:

#         if len(s) != len(t) : return False

#         seen1 = {}
#         for c1 in s :
#             seen1[c1] = 1 + seen1.get(c1, 0)
        
#         seen2 = {}
#         for c2 in t :
#             seen2[c2] = 1 + seen2.get(c2, 0)

#         if all(seen2.get(c,0) == seen1[c] for c in seen1) :
#             return True

#         return False 


class Solution():

    def isAnagram(self, s : str, t : str  ) -> bool:

        if len(s) != len(t):
            return False

        seen1 = {} #for s
        seen2 = {} #for t

        for c in s:
            seen1[c] = 1 + seen1.get(c,0)

        for c in t:
            seen2[c] = 1 + seen2.get(c,0)
        
        if all(seen1 == seen2 for c in seen2):
            return True
        return False






































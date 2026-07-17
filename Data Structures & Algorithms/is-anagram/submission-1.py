class Solution():

    def isAnagram(self, s : str, t : str  ) -> bool:

        if len(s) != len(t):
            return False
        S, T = {}, {}  #empty dictionaries are created

        for i in range(len(s)): #makes key - value pair for both dictionaries
            S[s[i]] =1+ S.get(s[i],0)
            T[t[i]] =1+ T.get(t[i],0)

        for c in S:
            if S[c] != T.get(c,0): #checks if for same char both dict has same value
                return False
        
        return True
# class Solution:
#     def isValid(self, s: str) -> bool:
        
#         seen = {'}':'{',')':'(',']':'['} # mapped every closing(key) with opening(value)
#         stack = [] #stack as a dynamic array
#         for c in s:

#             if c in seen :
#                 if stack and stack[-1] == seen[c] :
#                     stack.pop()
#                 else :
#                     return False

#             else :
#                 stack.append(c)
#         return True if not stack else False
        

# class Solution:
#     def isValid(self, s: str) -> bool:

        # seen = {'}':'{',']':'[',')':'('}

        # stack = []

        # for c in s :
        #     if c in seen :
        #         if stack and stack[-1]==seen[c]:
        #             stack.pop()

        #         else :
        #             return False
                    
        #     else :
        #         stack.append(c)
        # return True if not stack else False #if stack at end becomes empty


class Solution:
    def isValid(self, s: str) -> bool:
        seen = {'}':'{',']':'[',')':'('}
        stack = []

        for c in s :
            if c in seen:
                if stack and stack[-1]==seen[c] :
                    stack.pop()
                else :
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        


class Solution:
    def isValid(self, s: str) -> bool:
        hmap={'}':'{',']':'[',')':'('}
        stack=[]
        for c in s:
            if c in hmap:
                if stack and stack[-1]==hmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False


class Solution:
    def isValid(self, s: str) -> bool:
        hmap={'}':'{',']':'[',')':'('}
        stack=[]
        for c in s:
            if c in hmap:#for sure it's closing as it checks key
                if stack and stack[-1]==hmap[c]:
                    stack.pop()
                else:
                    return False

            else:#for sure it's opening
                stack.append(c)
        return True if not stack else False























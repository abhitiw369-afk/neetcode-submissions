# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
        # stack = []
        # for s in tokens :
        #     if s=='+' :
        #         stack.append(int(stack.pop()+stack.pop()))
        #     elif s=='-' :
        #         a,b = stack.pop(),stack.pop()
        #         stack.append(int(b-a))
        #     elif s=='*' :
        #         stack.append(int(stack.pop()*stack.pop()))
        #     elif s=='/' :
        #         a,b = stack.pop(),stack.pop()
        #         stack.append(int(b/a))
            
        #     else :
        #         stack.append(int(s))
        
        # return stack[0]


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for s in tokens :
            if s == '+':
                stack.append(stack.pop()+stack.pop())
            elif s == '-':
                a, b = stack.pop(),stack.pop()
                stack.append(b-a)
            elif s == '*':
                stack.append(stack.pop()*stack.pop())
            elif s == '/':
                a,b = stack.pop(),stack.pop()
                stack.append(int(b/a))
            else :
                stack.append(int(s))
        return stack[-1]



class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i == '+':
                stack.append(stack.pop()+stack.pop())
            elif i == '*':
                stack.append(stack.pop()*stack.pop())
            elif i == '/':
                a,b=stack.pop(),stack.pop()
                stack.append(int(b/a))
            elif i == '-':
                a,b=stack.pop(),stack.pop()
                stack.append(int(b-a))
            else:
                stack.append(int(i))
        return stack[-1]



















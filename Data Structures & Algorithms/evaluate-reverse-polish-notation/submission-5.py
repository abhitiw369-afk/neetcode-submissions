class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens :
            if s=='+' :
                stack.append(int(stack.pop()+stack.pop()))
            elif s=='-' :
                a,b = stack.pop(),stack.pop()
                stack.append(int(b-a))
            elif s=='*' :
                stack.append(int(stack.pop()*stack.pop()))
            elif s=='/' :
                a,b = stack.pop(),stack.pop()
                stack.append(int(b/a))
            
            else :
                stack.append(int(s))
        
        return stack[0]

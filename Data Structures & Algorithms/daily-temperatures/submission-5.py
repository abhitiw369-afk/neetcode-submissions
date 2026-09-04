# class Solution:
#     def dailyTemperatures(self, temp: List[int]) -> List[int]:
        
        # res = [0]*len(temp)
        # stack = []

        # for i,t in enumerate(temp) :
        #     while stack and t > stack[-1][0] :
        #         stackT,stackI = stack.pop()
        #         res[stackI] = i - stackI
        #     stack.append([t,i])
        # return res


class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:

        arr = [0]*len(temp)
        stack = []

        for i, t in enumerate(temp):
            while stack and t > stack[-1][0]:
                sT,sI=stack.pop()
                arr[sI] = i - sI
            stack.append([t,i])
        return arr

        



class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res=[0]*len(temp)
        stack=[]
        for i,t in enumerate(temp):
            while stack and t > stack[-1][0]:
                ST,SI=stack.pop()
                res[SI]=i-SI
            stack.append([t,i])
        return res

















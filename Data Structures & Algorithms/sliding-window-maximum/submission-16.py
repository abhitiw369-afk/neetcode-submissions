# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         op = []
#         q=collections.deque() #stores ind in monotonically dec ordr
#         l,r=0,0

#         while r < len(nums):
#             #pop smlr vls frm top or rt if grtr comes
#             while q and nums[q[-1]] < nums[r]:
#                 q.pop() #remove from rt
#             q.append(r) #we store indices

#             #remove the out of bound vals from lft
#             if l > q[0]: #This line removes indices that are no longer inside the current window.
#                 q.popleft()

#             #to check valid window
#             if (r+1)>=k: #"Have I reached a complete window of size k yet?
#                 op.append(nums[q[0]]) #append value
#                 l+=1
#             r+=1

#         return op





# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         op=[]
#         deq=collections.deque() 
#         #deque that store indices

#         l,r=0,0

#         while r < len(nums):
#             while deq and nums[deq[-1]]<nums[r]:
#                 deq.pop()
#             deq.append(r)#we put indices in que

#             if l>deq[0]: 
#                 #if l incremented,and we've done job with first deq ele, remove it from left
#                 deq.popleft()

#             if (r-l+1)>=k:
#                 op.append(nums[deq[0]]) 
#                 #left most value is always greater
#                 l+=1
#             r+=1
#             #we're just sliding window, with fixed size
#         return op




class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res =[]

        deq= collections.deque()

        l,r=0,0
        while r<len(nums):

            while deq and nums[deq[-1]]<nums[r]:
                deq.pop()   
            deq.append(r)

            if l > deq[0]:
                deq.popleft()
            
            if (r-l+1)==k:
                res.append(nums[deq[0]])
                l+=1
            r+=1

        return res




















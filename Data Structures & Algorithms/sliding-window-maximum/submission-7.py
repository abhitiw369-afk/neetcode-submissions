class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        op = []
        q=collections.deque() #stores ind in monotonically dec ordr
        l,r=0,0

        while r < len(nums):
            #pop smlr vls frm top or rt if grtr comes
            while q and nums[q[-1]] < nums[r]:
                q.pop() #remove from rt
            q.append(r) #we store indices

            #remove the out of bound vals from lft
            if l > q[0]: #This line removes indices that are no longer inside the current window.
                q.popleft()

            #to check valid window
            if (r+1)>=k: #"Have I reached a complete window of size k yet?
                op.append(nums[q[0]]) #append value
                l+=1
            r+=1

        return op


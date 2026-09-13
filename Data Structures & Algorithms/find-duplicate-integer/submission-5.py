class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0 #pts to indices as treating them as values
        while True:
            #here moving pointer in form of nums[slow] is beacuse due to we consider values as pointers
            #we do this here becasue this is list given and we treated it like a LL
            slow = nums[slow] #move slow one step, no of steps = no of nums 
            fast = nums[nums[fast]]
            if slow == fast :
                break

        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2 :
                return slow




class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        f,s=0,0
        while True: #because there'll definitely existing collision
            f=nums[nums[f]]
            s=nums[s]
            if f==s:
                break
        
        s1=0
        while True:
            s1=nums[s1]
            s=nums[s]
            if s1==s:
                return s1

        


















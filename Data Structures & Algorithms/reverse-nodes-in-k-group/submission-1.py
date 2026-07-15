# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        grpPrev = dummy

        while True :
            kth = self.getKth(grpPrev,k)
            if not kth :
                break  #if kth position is not valid
            grpNxt = kth.next

            #reversing k- groups
            prev, curr = kth.next, grpPrev.next

            while curr != grpNxt:
                temp = curr.next
                curr.next = prev 
                prev = curr
                curr = temp

            #updating links 
            temp = grpPrev.next
            grpPrev.next = kth
            grpPrev = temp

        return dummy.next




    def getKth(self, curr, k): 
        while curr and k > 0 :
            curr = curr.next
            k -= 1
        return curr

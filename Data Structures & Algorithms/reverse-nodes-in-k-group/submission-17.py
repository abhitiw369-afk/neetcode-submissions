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


















class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        grpPrv=dummy

        
        while True:
            kth=self.getKth(grpPrv,k)
            if not kth:
                break
            
            grpNxt=kth.next
            prev,curr=grpNxt,grpPrv.next

            while curr!=grpNxt:
                after=curr.next
                curr.next=prev
                prev=curr
                curr=after

            tmp=grpPrv.next
            grpPrv.next=kth
            grpPrv=tmp

            
        return dummy.next

    def getKth(self,curr,k):
        while curr and k>0:
            curr=curr.next
            k-=1
        return curr
        







class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        grpPrv=dummy

        while True:
            kth=self.getkth(grpPrv,k)
            if not kth: break

            grpNxt=kth.next
            #we've set our boundaries for k groups, now pointers for reversion each node at a time
            prev,curr=grpNxt,grpPrv.next

            while curr!=grpNxt:
                after=curr.next
                curr.next=prev
                prev=curr
                curr=after

            #after reversing k nodes in a grp we've to update boundaries
            tmp=grpPrv.next
            grpPrv.next=kth
            grpPrv=tmp

        return dummy.next

    def getkth(self,curr,k):
        while curr and k>0:
            curr=curr.next
            k-=1
        return curr



















class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head) #potentially head can change
        grpPrv=dummy #left boundary for k-nodes
        while True:
            kth=self.getkth(grpPrv,k)
            if not kth: break

            grpNxt=kth.next #right boundary for k-nodes

            curr=grpPrv.next
            prev=grpNxt

            while curr!=grpNxt: #reversal in k nodes at a time
                after=curr.next
                curr.next=prev
                prev=curr
                curr=after
            
            #Now we have to update our boundaries and repeat it again
            tmp=grpPrv.next
            grpPrv.next=kth
            grpPrv=tmp

        return dummy.next



    def getkth(self,curr,k):
        while curr and k>0:
            curr=curr.next
            k-=1
        return curr

        

























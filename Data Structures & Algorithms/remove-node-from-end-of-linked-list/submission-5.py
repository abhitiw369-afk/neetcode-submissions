# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left = dummy

        right = head

        while n>0 and right:
            right= right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next




class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        dummy=ListNode(0,head)
        temp1=dummy
        #temp will be at the node which we want to remove
        while n>0 and temp:
            temp=temp.next
            n-=1
        
        #now we've take our temp1 to the node just before the targeted node
        while temp:
            temp1=temp1.next
            temp=temp.next

        temp1.next=temp1.next.next

        return dummy.next



















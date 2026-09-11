# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #finding middle of 2 halves
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        #reverse second half
        before = None
        temp = slow.next
        slow.next = None

        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        
        #merge two halves
        first = head
        second = before

        while second:
            after = first.next
            temp = second.next

            first.next = second
            second.next = after

            first = after
            second = temp












class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find middle of list for splitting
        fast,slow=head.next,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next

        #breaking list from middle and reversing 2nd half
        temp=slow.next
        slow.next=None
        before=None

        while temp:
            after=temp.next
            temp.next=before
            before=temp
            temp=after
        
        #merging two lists in required order
        first=head
        second=before

        while second:
            temp1=first.next
            temp2=second.next

            first.next=second
            second.next=temp1

            first=temp1
            second=temp2






















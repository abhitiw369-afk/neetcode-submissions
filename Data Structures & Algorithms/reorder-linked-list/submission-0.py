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












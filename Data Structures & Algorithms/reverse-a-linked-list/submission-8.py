# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        before = None

        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after

        return before




class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        before=None

        while curr:
            after=curr.next
            curr.next=before
            before=curr
            curr=after
        return before

        
















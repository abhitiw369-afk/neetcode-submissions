# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            #new digit
            val = v1 + v2 + carry       
            carry = val//10
            val = val % 10
        
            curr.next = ListNode(val)

            #update ptrs
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        temp=dummy

        carry=0

        while l1 or l2 or carry:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0

            val=v1+v2+carry
            carry=val//10 #carry to next node
            val=val%10 #digit to put in the current node

            temp.next=ListNode(val) #created a new node for val and linked to dummy's next/temp's next
            temp=temp.next #moving temp ahead so to join nodes

            l1=l1.next if l1 else None
            l2=l2.next if l2 else None

        return dummy.next





class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy=ListNode()
        temp=dummy
        carry=0

        while l1 or l2 or carry:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            val=v1+v2+carry

            carry=val//10
            val=val%10

            temp.next=ListNode(val)

            temp=temp.next

            l1=l1.next if l1 else None
            l2=l2.next if l2 else None

        return dummy.next














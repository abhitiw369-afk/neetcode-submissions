# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedList = []

            for i in range(0, len(lists), 2): #i=1: 1,2 : merge, then i =3: 3,4 : merge
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None #valid list + none list = valid combo
                mergedList.append(self.mergeList(l1,l2)) #noe empty list mein append kar rahe
            lists = mergedList #lists got updated and finally only 1 list in it
        return lists[0] #[[0-th index list]]

    def mergeList(self,list1,list2):  #method for merging 2 sorted LL
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val :
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1

        else:
            tail.next = list2


        return dummy.next
















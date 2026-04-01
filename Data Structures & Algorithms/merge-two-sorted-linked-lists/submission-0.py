# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        if not list2:
            return list1
        if not list1 and not list2:
            return None

        p1 = list1
        p2 = list2
        dummy = ListNode(-1)
        head = dummy

        while p1 and p2:
            if p1 and p2 and p1.val <= p2.val:
                dummy.next = p1
                p1 = p1.next
            elif p1 and p2 and p1.val > p2.val:
                dummy.next = p2
                p2 = p2.next
            dummy = dummy.next
        if p1:
            dummy.next = p1
        if p2:
            dummy.next = p2

        return head.next



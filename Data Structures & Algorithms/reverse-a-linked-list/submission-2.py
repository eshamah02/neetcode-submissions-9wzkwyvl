# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        p1 = head 
        p2 = head.next

        while p2:
            if p1 == head:
                p1.next = None
            extra = p2.next
            p2.next = p1
            p1 = p2
            p2 = extra
            
        return p1

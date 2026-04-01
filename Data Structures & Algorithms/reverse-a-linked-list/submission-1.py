# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head
        p1 = head if head else None
        p2 = head.next if head.next else None
        print(f"p1: {p1.val}")
        print(f"p2: {p2.val}")
        while p2:
            if p1 == head:
                print(f"p1 is head, setting p1.next to None, {p1.val}")
                p1.next = None
            extra = p2.next
            p2.next = p1
            p1 = p2
            p2 = extra
            
        return p1

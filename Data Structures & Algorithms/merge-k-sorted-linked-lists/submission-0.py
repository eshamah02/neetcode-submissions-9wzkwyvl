# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None
        # dummy_head = ListNode(0, None)
        # new_list = dummy_head
        # for i in range(len(lists) - 1):
        #     new_list.next = self.mergeTwoLists(lists[i], lists[i + 1])

        # return dummy_head.next
        for i in range(1, len(lists)):
            lists[i] = self.mergeTwoLists(lists[i - 1], lists[i])
        
        return lists[-1]

    def mergeTwoLists(self, list1, list2):
        dummy_head = ListNode(0, None)
        i = list1
        j = list2
        k = dummy_head

        while i and j:
            if i.val <= j.val:
                k.next = i
                i = i.next
            else:
                k.next = j
                j = j.next
            k = k.next

        if i:
            k.next = i
        if j:
            k.next = j
        
        return dummy_head.next

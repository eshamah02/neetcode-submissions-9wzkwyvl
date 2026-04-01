class Node:

    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr_idx = 0
        curr_node = self.head.next
        while curr_node:
            if curr_idx == index:
                return curr_node.val
            curr_node = curr_node.next
            curr_idx += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if new_node.next is None:
            self.tail = new_node

        

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        curr_idx = 0
        curr_node = self.head
        while curr_idx < index and curr_node:
            curr_idx += 1
            curr_node = curr_node.next
        if curr_node and curr_node.next:
            if curr_node.next == self.tail:
                self.tail = curr_node
            curr_node.next = curr_node.next.next
            return True
        return False
            

        

    def getValues(self) -> List[int]:
        values = []
        curr_node = self.head.next

        while curr_node:
            values.append(curr_node.val)
            curr_node = curr_node.next
        
        return values
        

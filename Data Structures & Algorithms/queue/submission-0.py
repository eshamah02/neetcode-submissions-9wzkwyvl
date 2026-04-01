class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.left = Node(-1)
        self.right = Node(-1)
        self.left.next = self.right
        self.right.prev = self.left

    def isEmpty(self) -> bool:
        if self.left.next == self.right and self.right.prev == self.left:
            return True
        else:
            return False
        

    def append(self, value: int) -> None:
        new_node = Node(value)
        prev = self.right.prev
        next = self.right
        prev.next = new_node
        next.prev = new_node
        new_node.next = next
        new_node.prev = prev

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        prev = self.left
        next = self.left.next
        prev.next = new_node
        next.prev = new_node
        new_node.next = next
        new_node.prev = prev
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        last_val = self.right.prev.val
        prev = self.right.prev.prev
        next = self.right
        prev.next = next
        next.prev = prev
        return last_val


    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        beg_val = self.left.next.val
        prev = self.left
        next = self.left.next.next
        prev.next = next
        next.prev = prev
        return beg_val
        

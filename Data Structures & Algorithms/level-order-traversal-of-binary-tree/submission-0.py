# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        res = []
        if root:
            queue.append(root)
            res.append([root.val])

        while len(queue) > 0:
            lev = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                    lev.append(curr.left.val)
                if curr.right:
                    queue.append(curr.right)
                    lev.append(curr.right.val)
            if lev:
                res.append(lev)
        
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur_val = root.val
        cur_idx = 0

        def inorder(node):
            nonlocal cur_val, cur_idx
            if not node:
                return
            
            inorder(node.left)
            cur_idx += 1
            if cur_idx == k:
                cur_val = node.val
                return
            inorder(node.right)

        inorder(root)
        return cur_val
            
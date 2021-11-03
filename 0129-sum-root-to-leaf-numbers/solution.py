# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = []
        def travel(n, node):
            n = n * 10 + node.val
            if (node.left == None and node.right == None):
                nums.append(n)
            if (node.left):
                travel(n, node.left)
            if (node.right):
                travel(n, node.right)
        travel(0, root)
        return sum(nums)
                
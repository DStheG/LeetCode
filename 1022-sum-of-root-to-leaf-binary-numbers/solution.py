# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def travel(root, literal):
            if (root == None):
                return 0
            val = (literal << 1) + root.val
            if (root.left == None and root.right == None):
                return val
            else:
                return travel(root.left, val) + travel(root.right, val)
        return travel(root, 0)
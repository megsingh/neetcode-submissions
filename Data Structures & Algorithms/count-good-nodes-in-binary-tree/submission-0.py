# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def goodNodesHelper(self, root, max_value):
        if not root:
            return 0

        if root.val >= max_value:
            return 1 + self.goodNodesHelper(root.left, root.val) + self.goodNodesHelper(root.right, root.val)

        return self.goodNodesHelper(root.left, max_value) + self.goodNodesHelper(root.right, max_value)
            

    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesHelper(root, float('-inf'))        
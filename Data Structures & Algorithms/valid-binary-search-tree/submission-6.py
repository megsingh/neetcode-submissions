# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isValidBSTHelper(self, root, left, right):
        if not root:
            return True

        if left < root.val < right:
            return self.isValidBSTHelper(root.left, left, root.val) and self.isValidBSTHelper(root.right, root.val, right)

        return False

        


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root, float("-inf"), float("inf"))
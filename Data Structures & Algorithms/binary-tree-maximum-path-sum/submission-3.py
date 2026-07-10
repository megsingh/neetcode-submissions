# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxPathSumHelper(self, root):
        if not root:
            return float('-inf'), 0

        if not root.right and not root.left:
            return root.val, root.val

        left_max, left_sum = self.maxPathSumHelper(root.left)
        right_max, right_sum = self.maxPathSumHelper(root.right)

        max_till_now = max(max(left_max, right_max), max(root.val, left_sum+right_sum+root.val) , max(left_sum+root.val, right_sum+root.val))
        sum_with_node = max(root.val, root.val+max(left_sum, right_sum))

        return max_till_now, sum_with_node

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.maxPathSumHelper(root)[0]
        
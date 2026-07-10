# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalancedHelper(self, root):
        if not root:
            return [0,True]

        left_node = self.isBalancedHelper(root.left)
        right_node = self.isBalancedHelper(root.right)
        left_height = left_node[0]
        right_height = right_node[0]

        is_balanced = True
        if abs(left_height - right_height) >1 or not left_node[1] or not right_node[1]:
            is_balanced = False

        return max(left_height, right_height)+1, is_balanced


    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        return self.isBalancedHelper(root)[1]
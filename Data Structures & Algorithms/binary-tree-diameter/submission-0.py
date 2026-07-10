# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTreeHelper(self, root) -> (int, int):
        if not root:
            return (0,0)

        left_node = self.diameterOfBinaryTreeHelper(root.left)
        right_node = self.diameterOfBinaryTreeHelper(root.right)

        left_diameter = left_node[0]
        right_diameter = right_node[0]
        left_height = left_node[1]
        right_height = right_node[1]
        curr_diameter = left_height + right_height

        max_diameter = max(max(left_diameter, right_diameter), curr_diameter)
        max_height = max(left_height, right_height)+1

        return max_diameter, max_height

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        max_d, height = self.diameterOfBinaryTreeHelper(root)
        return max_d

        
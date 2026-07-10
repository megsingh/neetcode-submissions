# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def lowestCommonAncestorHelper(self, root: TreeNode, p: TreeNode, q: TreeNode):
        if not root:
            return root, False, False

        if p.val > root.val and q.val>root.val:
            right_node, has_p, has_q = self.lowestCommonAncestorHelper(root.right, p, q)
            if has_p and has_q:
                return right_node, True, True
        
        elif p.val < root.val and q.val < root.val:
            left_node, has_p, has_q = self.lowestCommonAncestorHelper(root.left, p, q)
            if has_p and has_q:
                return left_node, True, True

        else:
            return root, True, True     


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        res, has_p, has_q = self.lowestCommonAncestorHelper(root, p, q)
        return res;
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()

        q.append(root)
        q.append(None)
        res = []

        sub_arr = []
        while q:
            front = q.popleft()
            if not front:
                res.append(sub_arr)
                sub_arr = []

                if len(q)==0:
                    return res
                
                q.append(None)
                continue

            sub_arr.append(front.val)
            if front.left:
                q.append(front.left)

            if front.right:
                q.append(front.right)

            

            
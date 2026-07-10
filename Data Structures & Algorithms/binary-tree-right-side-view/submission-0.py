# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque()

        q.append(root)
        q.append(None)
        res = []
        while q:
            front = q.popleft()
            if not front:
                if len(q)==0:
                    return res
                
                q.append(None)
                continue            
            
            if q and q[0] == None:
                res.append(front.val)
            if front.left:
                q.append(front.left)

            if front.right:
                q.append(front.right)

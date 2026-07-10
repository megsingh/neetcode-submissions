# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res = []

        queue = deque()
        queue.append(root)

        while queue:
            front = queue.popleft()

            if front == None:
                res.append("N")
                continue

            res.append(str(front.val))
            if front.left:
                queue.append(front.left)
            else:
                queue.append(None)

            if front.right:
                queue.append(front.right)
            else:
                queue.append(None)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0:
            return None

        values = data.split(",")
        queue = deque()
        root = TreeNode(int(values[0]))
        i=1
        queue.append(root)
        n = len(data)

        while queue:
            front = queue.popleft()

            if i< n and values[i]!="N":
                front.left = TreeNode(int(values[i]))
                queue.append(front.left)
            i+=1

            if i< n and values[i]!="N":
                front.right = TreeNode(int(values[i]))
                queue.append(front.right)
            i+=1

        return root






















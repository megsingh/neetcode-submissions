"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        node_map = {None:None}

        curr = head
        while curr:
            temp = Node(curr.val)
            node_map[curr] = temp
            curr = curr.next

        curr=head
        while curr:
            temp = node_map[curr]
            temp.next = node_map[curr.next]
            temp.random = node_map[curr.random]
            curr = curr.next

        return node_map[head]
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 

    def mergeLists(self, list1, list2)   -> Optional[ListNode]:
        dummynode = ListNode(0)
        curr = dummynode

        c1 = list1
        c2 = list2

        while c1 and c2:
            if c1.val <= c2.val:
                curr.next = c1
                c1 = c1.next
            else:
                curr.next = c2
                c2 = c2.next
            curr = curr.next
        
        curr.next = c1 if c1 else c2
        return dummynode.next
        
            

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        for i in range(1, len(lists)):
            lists[i] = self.mergeLists(lists[i-1], lists[i])

        return lists[-1]
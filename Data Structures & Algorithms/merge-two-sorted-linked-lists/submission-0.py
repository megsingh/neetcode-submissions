# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        prev = None
        l1,l2 = list1, list2
        if l1 == None:
            return l2
        if l2==None:
            return l1

        while l1!=None and l2!=None:
            if l1.val < l2.val:
                if head == None:
                    head = l1 
                    prev = head
                else:
                    prev.next = l1
                    prev = l1
                l1=l1.next
            else:
                if head == None:
                    head = l2
                    prev = head
                else:
                    prev.next = l2
                    prev = l2  
                l2=l2.next  

        if l1!=None:
            
            prev.next = l1
        else:
            prev.next = l2

        return head

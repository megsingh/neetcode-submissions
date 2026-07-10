# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr!=None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head = prev
        return head
        

    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast, prev = head, head, None

        if head.next==None or head.next.next==None:
            return

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        head2 = self.reverseList(slow)
        
        curr = head
        curr2 = head2
        while curr!=None:
            temp = curr.next
            temp2 = curr2.next
            curr.next = curr2
            curr = temp
            if curr:
                curr2.next = curr
            curr2 = temp2

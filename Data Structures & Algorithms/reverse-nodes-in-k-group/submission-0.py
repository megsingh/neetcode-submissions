# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseList(self, head, tail) -> (Optional[ListNode], Optional[ListNode]):
        curr = head
        prev = None

        while curr:
            nextN = curr.next
            curr.next = prev
            prev = curr
            curr = nextN

        return tail, head

        

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        prev_end = None

        while True:
            start = curr
            end = None
            count = k

            while curr and count:
                end = curr
                curr = curr.next
                count-=1
            if count>0:
                return head
            end.next = None
            if prev_end:
                prev_end.next = None

            reverse_start, reverse_end = self.reverseList(start, end)
            if reverse_end == head:
                head = reverse_start
            if prev_end:
                prev_end.next = reverse_start
            reverse_end.next = curr
            prev_end = reverse_end
            

          

            
                


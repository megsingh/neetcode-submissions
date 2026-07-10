# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        c1 = l1
        c2 = l2

        res = None
        head = None
        carry = 0
        while c1 and c2:
            sum_ = c1.val + c2.val + carry
            carry = sum_//10

            temp = ListNode(sum_%10)
            if res:
                res.next = temp
                res = res.next
            else:
                res = temp 
                head = temp

            c1 = c1.next
            c2 = c2.next
            

        curr = c1 if c1 else c2
        
        while curr:
            sum_ = curr.val + carry
            carry = sum_//10
            temp = ListNode(sum_%10)
            res.next = temp
            res = res.next
            curr = curr.next

        
        if carry>0:
            res.next = ListNode(carry)
        return head
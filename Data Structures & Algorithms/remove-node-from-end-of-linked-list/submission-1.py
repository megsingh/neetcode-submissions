# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        len_list = 1

        curr = head
        prev = None
        while curr.next!=None:
            prev = curr
            curr = curr.next
            len_list +=1

        if n == len_list:
            return head.next

        elif n == 1:
            prev.next = None
            return head
        else:
            nodeFromFront = len_list - n

            currN = head
            prevN = None
            
            while nodeFromFront>0:
                prevN = currN
                currN = currN.next
                nodeFromFront-=1

            
            prevN.next = currN.next
            currN.next = None

            return head




        

        

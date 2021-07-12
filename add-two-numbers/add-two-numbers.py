#    Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        v = l1.val + l2.val
        c = 0
        if v > 9: 
            c = 1
            v -= 10
        prev = ret = ListNode(v)
        l1 = l1.next
        l2 = l2.next
        
        while l1 or l2:
            v1 = 0 if l1 == None else l1.val
            v2 = 0 if l2 == None else l2.val

            v = v1 + v2 + c

            c = 0
            if v > 9: 
                c = 1
                v -= 10

            prev.next = ListNode(v)
            prev = prev.next  
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if c:
            prev.next = ListNode(c)
        return ret
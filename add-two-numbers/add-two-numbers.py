#    Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        c = 0
        
        ret = None
        while l1 or l2:
            v1 = 0 if l1 == None else l1.val
            v2 = 0 if l2 == None else l2.val
            v = v1 + v2 + c
            n = ListNode(v % 10)
            if (ret == None):
                ret = n
                prev = n
            else:
                prev.next = n
                prev = n
                
            c = v // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if c:
            prev.next = ListNode(c)
        return ret
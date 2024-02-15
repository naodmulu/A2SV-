# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        checker = set()
        trav = headA
        while trav:
            checker.add(trav)
            trav = trav.next
        
        trav = headB
        while trav:
            if trav in checker:
                return trav
            trav = trav.next
        return trav
        
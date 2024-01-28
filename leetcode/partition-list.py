# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        greater = ListNode()
        less = ListNode()
        trav = head
        l = less
        g = greater 
        while trav:
            if trav.val < x:
                l.next = trav
                l = trav
            elif trav.val >= x:
                g.next = trav
                g = trav
            trav = trav.next
        l.next = greater.next
        g.next = None
        return less.next
        
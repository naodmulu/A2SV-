# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        trav = head
        occur= set()

        while trav and trav.next:
            occur.add(trav)
            trav = trav.next
            if trav in occur:
                return trav
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        trav = head.next
        prev = head
        x = None
        while trav:
            if prev.val != trav.val:
                prev.next = trav
                prev = trav
            x = trav
            trav = trav.next


        if x and prev.val == x.val :
            prev.next = None
        return head
        
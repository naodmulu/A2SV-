# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dmmy_head = ListNode(0,head)
        f,s = dmmy_head.next,dmmy_head
        
        for _ in range(n):
            f = f.next
        while f:
            f,s = f.next,s.next
        
        s.next = s.next.next
        
        return dmmy_head.next
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        trav = head
        prev = None
        newNode = None
        while trav:
            newNode = ListNode(trav.val)
            newNode.next = prev
            prev = newNode
            trav = trav.next
        return newNode
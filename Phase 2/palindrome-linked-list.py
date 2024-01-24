# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        trav = head
        prev = None
        newNode = None
        while trav:
            newNode = ListNode(trav.val)
            newNode.next = prev
            prev = newNode
            trav = trav.next
        trav = head
        while trav:
            print(trav.val,newNode.val)
            if trav.val != newNode.val:
                return False
            trav= trav.next
            newNode= newNode.next
        return True
        
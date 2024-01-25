# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ansNode = ListNode(0,None)
        ans = ansNode
        while list1 and list2:
            
            if list1.val <= list2.val:
                # print(list1.val)
                newNode = ListNode(list1.val,None)
                ansNode.next = newNode
                ansNode = newNode
                list1 = list1.next
            else:
                newNode = ListNode(list2.val,None)
                ansNode.next = newNode
                ansNode = newNode
                list2 = list2.next
        if list1:
            ansNode.next = list1
        elif list2:
            ansNode.next = list2
        return ans.next

        
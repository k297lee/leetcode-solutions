# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        node = head.next
        prev = head
        prev.next = None
        
        while node:
            tmp_next = node.next
            node.next = prev
            prev = node
            node = tmp_next
        
        return prev
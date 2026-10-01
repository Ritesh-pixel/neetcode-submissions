# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Handle empty list
        if not head:
            return None
        
        # Dummy node simplifies edge cases
        dummy = ListNode(0, head)
        
        # Initialize tortoise and hare
        slow = fast = dummy
        
        # Create n-step gap
        for _ in range(n):
            fast = fast.next
        
        # Move both until hare reaches last node
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # Remove target node
        slow.next = slow.next.next
        
        return dummy.next

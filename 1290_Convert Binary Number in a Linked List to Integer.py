# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
     current=head
     decimal_val=0
     while current is not None:
        decimal_val = (decimal_val*2) + current.val
        current = current.next
     return decimal_val      
        
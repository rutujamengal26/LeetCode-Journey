# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if left == right:
            return head
        dummy = ListNode(0, head)
        sublist_prev = dummy
        for _ in range(left - 1):
         sublist_prev = sublist_prev.next
        curr = sublist_prev.next
        prev = None
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev=curr
            curr=nxt
        sublist_prev.next.next = curr
        sublist_prev.next = prev
        return dummy.next
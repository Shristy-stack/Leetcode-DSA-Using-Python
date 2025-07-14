# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev=None
        left, right= head,head
        while n!=0:
            right=right.next
            n-=1
        if right is None:
            return head.next
        while right:
            prev=left
            left=left.next
            right=right.next
        if prev is not None:
            prev.next=left.next
        left.next=None
        return head
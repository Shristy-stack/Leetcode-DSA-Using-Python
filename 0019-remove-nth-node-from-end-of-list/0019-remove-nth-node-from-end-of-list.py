# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        length=0
        while temp:
            temp=temp.next
            length+=1
        if length==1 and n==1:
            return None
        if n == length:
            return head.next
        temp,prev=head,None
        value=length-n
        while value!=0:
            prev=temp
            temp=temp.next
            value-=1
        prev.next=temp.next
        temp.next=None
        return head



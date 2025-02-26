# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashmap={}
        temp=head
        while(temp):
            if temp in hashmap:
                return True
            hashmap[temp]=temp.val
            temp=temp.next
        return False
        
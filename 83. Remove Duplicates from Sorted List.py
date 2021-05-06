# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        c=head
        while c and c.next :
            if c.val==c.next.val:
                c.next=c.next.next
            else:
                c=c.next
        return head

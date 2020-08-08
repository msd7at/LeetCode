# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy=pre=ListNode(0)
        dummy.next=head
        while head and head.next:
            if head.val==head.next.val:
                while head and head.next and head.val==head.next.val:
                    head=head.next
                head=head.next
                pre.next=head
            else:
                head=head.next
                pre=pre.next
        return dummy.next
                

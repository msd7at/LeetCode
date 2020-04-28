class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        prev= None
        while cur:
            next=cur.next
            cur.next= prev
            prev=cur
            cur=next
        return  prev
"""Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

Accepted
904,271
Submissions
1,489,341"""

# https://neetcode.io/problems/reverse-a-linked-list
# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

# Input: head = [0,1,2,3]
# Output: [3,2,1,0]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

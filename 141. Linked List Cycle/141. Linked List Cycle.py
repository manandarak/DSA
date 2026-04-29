#
# Problem: 141. Linked List Cycle
# Difficulty: Easy
# Link: https://leetcode.com/problems/linked-list-cycle/description/
# Language: python
# Date: 2026-04-29


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        

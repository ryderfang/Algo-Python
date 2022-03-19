#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        p_head = None
        p_tail = None
        q_head = None
        q_tail = None
        p = head
        while p != None:
            if p.val < x:
                p_head = p_head or p
                if p_tail != None:
                    p_tail.next = p
                    p_tail = p
                else:
                    p_tail = p
            else:
                q_head = q_head or p
                if q_tail != None:
                    q_tail.next = p
                    q_tail = p
                else:
                    q_tail = p
            p = p.next
        if p_tail != None:
            p_tail.next = q_head
        if q_tail != None:
            q_tail.next = None
        return p_head if p_head else q_head

# @lc code=end


#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
from xml.sax.handler import property_lexical_handler
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cnt = 0
        p = head
        pp = None
        pp_left = None
        p_left = None
        pp_right = None
        p_right = None
        while p != None:
            cnt += 1
            q = p.next
            if cnt == left:
                pp_left = pp if left > 1 else None
                p_left = p
            if cnt > left and cnt <= right:
                p.next = pp
            if cnt == right:
                pp_right = p
                p_right = q
            pp = p
            p = q
        if pp_left == None:
            head.next = p_right
            return pp_right
        else:
            pp_left.next = pp_right
            p_left.next = p_right
            return head
        
# @lc code=end


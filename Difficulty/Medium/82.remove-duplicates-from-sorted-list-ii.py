#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ret = None
        pp = None
        p = head
        while p != None:
            q = p.next
            if q != None and q.val == p.val:
                while q.next != None and q.next.val == q.val:
                    q = q.next
                p = q.next
                if pp != None:
                    pp.next = p
            else:
                ret = p if ret == None else ret
                pp = p
                p = q
        return ret
        
# @lc code=end


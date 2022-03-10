#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ret = None
        pp = None
        p = head
        q = p.next
        while q != None:
            dup = False
            while q!= None and q.val == p.val:
                dup = True
                q = q.next
            if ret == None:
                ret = q if dup else head
            
            q = p.next
        return ret


        
# @lc code=end


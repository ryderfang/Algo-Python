#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        p = head
        q = head.next
        ans = q
        while p != None and q != None:
            tmp = q.next
            q.next = p
            # forward
            if tmp == None:
                p.next = None
                break
            elif tmp.next == None:
                p.next = tmp
            else:
                p.next = tmp.next
            p = tmp
            q = tmp.next
        return ans

# @lc code=end


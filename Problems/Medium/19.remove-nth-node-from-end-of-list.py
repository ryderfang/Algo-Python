#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        sz = 0
        p = head
        while p != None:
            p = p.next
            sz += 1
        p = head
        if sz == n:
            head = head.next
        for i in range(sz-n-1):
            p = p.next
        if p.next != None:
            p.next = p.next.next
        return head
# @lc code=end

# amazing
"""
Accepted
208/208 cases passed (12 ms)
Your runtime beats 100 % of python3 submissions
Your memory usage beats 14.83 % of python3 submissions (14.3 MB)
"""

# @lc comment
# 双指针解法非常秀
# 先将 fast 指针移动到第 n 位，slow 指针置于开头
# 那么同步移动 fast 到结尾时，slow 正好是倒数 n 位


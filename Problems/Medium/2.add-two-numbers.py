#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        sum = 0
        result = ListNode()
        nxt = result
        while l1 != None and l2 != None:
            p = nxt
            sum = l1.val + l2.val + carry
            if sum < 10:
                p.val = sum
                carry = 0
            else:
                p.val = sum % 10
                carry = 1
            nxt = ListNode()
            p.next = nxt
            l1 = l1.next
            l2 = l2.next
        last = l1 if l1 != None else l2
        while last != None:
            p = nxt
            sum = last.val + carry
            if sum < 10:
                p.val = sum
                carry = 0
            else:
                p.val = sum % 10
                carry = 1
            nxt = ListNode()
            p.next = nxt
            last = last.next
        if carry > 0:
            p = nxt
            p.val = carry
            p.next = None
        else:
            p.next = None
        return result

# @lc code=end


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
        result = l1
        last = l1
        while l1 != None:
            if l2 != None:
                sum = l1.val + l2.val + carry
                l2 = l2.next
            else:
                sum = l1.val + carry
            l1.val = sum % 10
            carry = 1 if sum >= 10 else 0
            last = l1
            l1 = l1.next
        if l2 != None:
            last.next = l2
        while l2 != None:
            sum = l2.val + carry
            l2.val = sum % 10
            carry = 1 if sum >= 10 else 0
            last = l2
            l2 = l2.next
        if carry > 0:
            temp = ListNode()
            temp.val = carry
            last.next = temp
        return result

# @lc code=end


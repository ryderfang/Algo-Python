#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        sz = 0
        p = head
        tail = head
        while p != None:
            sz += 1
            if p.next == None:
                tail = p
            p = p.next
        if sz < 2:
            return head
        k = k % sz
        if k == 0:
            return head
        cnt = 0
        p = head
        q = None
        while p != None:
            cnt += 1
            if cnt == (sz - k):
                q = p
                break
            p = p.next
        tail.next = head
        ret = q.next
        q.next = None
        return ret

        
# @lc code=end


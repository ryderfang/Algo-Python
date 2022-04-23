#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        tmp = []
        def _in_order(node):
            if node != None:
                _in_order(node.left)
                tmp.append(node)
                _in_order(node.right)

        def _quick_sort(b, e):
            i, j = b, e
            x = tmp[(i + j) // 2]
            while True:
                while tmp[i].val < x.val:
                    i += 1
                while tmp[j].val > x.val:
                    j -= 1
                if i <= j:
                    tmp[i].val, tmp[j].val = tmp[j].val, tmp[i].val
                i += 1
                j -= 1
                if i >= j:
                    break
            if i < e:
                _quick_sort(i, e)
            if j > b:
                _quick_sort(b, j)
        
        _in_order(root)
        _quick_sort(0, len(tmp) - 1)
        
# @lc code=end


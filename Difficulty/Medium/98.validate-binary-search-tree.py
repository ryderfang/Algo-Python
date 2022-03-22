#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        def _getNodes(rt):
            if rt == None:
                return []
            tmp = _getNodes(rt.left)
            tmp.append(rt.val)
            tmp += _getNodes(rt.right)
            return tmp
        arr += _getNodes(root)
        ret = True
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]:
                ret = False
                break
        return ret
        
# @lc code=end


#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [[-1 for j in range(n + 1)] for i in range(n + 1)]
        def _buildTree(i, j):
            if i > j:
               return 1
            if dp[i][j] >= 0:
               return dp[i][j]
            if i == j:
                dp[i][i] = 1
                return 1
            ans = 0
            for t in range(i, j + 1):
               left = _buildTree(i, t - 1)
               right = _buildTree(t + 1, j)
               ans += left * right
            dp[i][j] = ans
            return ans
        return _buildTree(1, n)
# @lc code=end


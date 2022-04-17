#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from Codebase._CommonUtils.tree_node import TreeNode

from typing import List, Optional
import itertools
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = [[None for j in range(n + 1)] for i in range(n + 1)]
        # 笛卡尔积
        def _getProduct(val, left, right):
            arr = []
            for x in itertools.product(left, right):
                temp = TreeNode(val)
                temp.left = x[0]
                temp.right = x[1]
                arr.append(temp)
            return arr
        # [i, j] 范围内构造 BST
        def _buildTree(i, j):
            if i > j:
                return [None]
            if dp[i][j] != None:
                return dp[i][j]
            if i == j:
                node = TreeNode(i)
                dp[i][j] = [node]
                return dp[i][j]
            
            tmp = []
            for t in range(i, j + 1):
                left = _buildTree(i, t - 1)
                right = _buildTree(t + 1, j)
                tmp.extend(_getProduct(t, left, right))
            # for tt in tmp:
            #     print(i, j, TreeNode.tree_to_array(tt))
            dp[i][j] = tmp
            return tmp
        _buildTree(1, n)
        return dp[1][n]
        
# @lc code=end


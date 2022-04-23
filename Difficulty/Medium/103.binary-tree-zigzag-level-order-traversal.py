#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def _larger(n):
            for i in range(len(ans), n + 1):
                ans.append([])
        def _traversal(node, depth):
            if node != None:
                _larger(depth)
                tmp = ans[depth]
                tmp.append(node.val)
                _traversal(node.left, depth + 1)
                _traversal(node.right, depth + 1)
        _traversal(root, 0)
        reverse = False
        for x in ans:
            if reverse:
                x.reverse()
            reverse = not reverse
        return ans
# @lc code=end


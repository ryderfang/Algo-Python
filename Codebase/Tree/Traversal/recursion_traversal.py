#! /usr/local/bin/python3

from typing import Optional, List
from functools import reduce
import os
import sys

sys.path.append(os.getcwd())
from Codebase.Tree.tree_node import TreeNode

# 树的遍历，递归实现
## 先序遍历
def preOrder(root: Optional[TreeNode]) -> List[int]:
    ans = []
    def _traversal(node):
        if node == None:
            return
        ans.append(node.val)
        _traversal(node.left)
        _traversal(node.right)
    _traversal(root)
    return ans

## 中序遍历
def inOrder(root: Optional[TreeNode]) -> List[int]:
    ans = []
    def _traversal(node):
        if node == None:
            return
        _traversal(node.left)
        ans.append(node.val)
        _traversal(node.right)
    _traversal(root)
    return ans

## 后序遍历
def postOrder(root: Optional[TreeNode]) -> List[int]:
    ans = []
    def _traversal(node):
        if node == None:
            return
        _traversal(node.left)
        _traversal(node.right)
        ans.append(node.val)
    _traversal(root)
    return ans

## 层次遍历
### 分层存放，[[0], [1, 2], ...]
def levelOrder1(root: Optional[TreeNode]) -> List[List[int]]:
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
    return ans

### 不分层，[0, 1, 2, ...]
def levelOrder2(root: Optional[TreeNode]) -> List[int]:
    tmp = levelOrder1(root)
    ans = reduce(lambda x, y: x + y, tmp)
    return ans

if __name__ == "__main__":
    cases = [
        [1,3,None,None,2],
        [3,1,4,None,None,2],
        [10,5,15,0,8,13,20,2,-5,6,9,12,14,18,25],
        [3,9,20,None,None,15,7],
    ]
    for x in cases:
        root = TreeNode.array_to_tree(x)
        print(preOrder(root))
        print(inOrder(root))
        print(postOrder(root))
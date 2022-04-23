#! /usr/local/bin/python3

from typing import Optional, List
from functools import reduce
import os
import sys

sys.path.append(os.getcwd())
from Codebase.Tree.tree_node import TreeNode

# 树的遍历，非递归实现
## 先序遍历【栈实现】
def iterativePreOrder(root: Optional[TreeNode]) -> List[int]:
    ans = []
    stack = [root]
    while len(stack):
        node = stack.pop()
        ans.append(node.val)
        # right child is pushed first so that left is processed first
        if node.right != None:
            stack.append(node.right)
        if node.left != None:
            stack.append(node.left)
    return ans

## 中序遍历【栈实现】
def iterativeInOrder(root: Optional[TreeNode]) -> List[int]:
    ans = []
    stack = []
    node = root
    while len(stack) or node != None:
        if node != None:
            stack.append(node)
            node = node.left
        else:
            node =  stack.pop()
            ans.append(node.val)
            node = node.right
    return ans

## 后序遍历【栈实现】
def iterativePostOrder(root: Optional[TreeNode]) -> List[int]:
    ans = []
    stack = []
    node = root
    last_node = None
    while len(stack) or node != None:
        if node != None:
            stack.append(node)
            node = node.left
        else:
            top = stack[-1]
            if top.right != None and last_node != top.right:
                node = top.right
            else:
                ans.append(top.val)
                last_node = stack.pop()
    return ans

## 层次遍历
### 分层存放，[[0], [1, 2], ...]
def levelOrder1(root: Optional[TreeNode]) -> List[List[int]]:
    ans = []
    return ans

### 不分层，[0, 1, 2, ...]【队列实现】
def levelOrder2(root: Optional[TreeNode]) -> List[int]:
    ans = []
    queue = [root]
    while len(queue):
        node = queue.pop(0)
        ans.append(node.val)
        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)
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
        # print(iterativePreOrder(root))
        # print(iterativeInOrder(root))
        print(iterativePostOrder(root))
import queue
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Array -> Tree
    @classmethod
    def array_to_tree(cls, data: List):
        sz = len(data)
        if sz == 0:
            return None
        root = cls(data[0])
        queue = [root]
        i = 1
        while len(queue) > 0 and i < sz:
            node = queue.pop(0)
            if data[i] != None:
                tmp = cls(data[i])
                node.left = tmp
                queue.append(tmp)
            i += 1
            if i >= sz:
                break
            if data[i] != None:
                tmp = cls(data[i])
                node.right = tmp
                queue.append(tmp)
            i += 1
        return root
    # Tree -> Array
    @classmethod
    def tree_to_array(cls, root):
        ans = []
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
            if node != None:
                ans.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                ans.append(None)
        # remove Nones at last
        while ans[-1] == None:
            ans.pop()
        return ans

if __name__ == "__main__":
    pass
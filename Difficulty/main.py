import importlib.util
import inspect
import glob, os
import json
import sys

sys.path.append(os.getcwd())
from Codebase.List.list_node import ListNode
from Codebase.Tree.tree_node import TreeNode

PROBLEM_NO = 102
PROBLEM_LV = '/Medium/'
cls = None

def load_module():
    global cls
    os.chdir(os.path.dirname(__file__))
    file_path = glob.glob(os.getcwd() + PROBLEM_LV + str(PROBLEM_NO) + '.*.py')[0]
    print(file_path)

    spec = importlib.util.spec_from_file_location(os.path.basename(file_path), file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    for member in inspect.getmembers(module):
        if member[0] == 'Solution':
            cls = member[1]
            break

def load_testcase():
    test_file = os.getcwd() + '/../Testcase/t' + str(PROBLEM_NO).zfill(2)
    lines = []
    with open(test_file) as f:
        lines = f.readlines()
    ans = []
    for l in lines:
        ans.append(json.loads(l))
    return ans

if __name__ == "__main__":
    load_module()
    sol = cls()
    # cases = load_testcase()
    cases = [
        [1,3,None,None,2],
        [3,1,4,None,None,2],
        [10,5,15,0,8,13,20,2,-5,6,9,12,14,18,25],
        [3,9,20,None,None,15,7],
    ]
    for x in cases:
        root = TreeNode.array_to_tree(x)
        ans = sol.levelOrder(root)
        print(ans)
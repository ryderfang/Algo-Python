import importlib.util
import inspect
import glob, os
import json
import sys

sys.path.append(os.getcwd())
from Codebase._CommonUtils.list_node import ListNode
from Codebase._CommonUtils.tree_node import TreeNode

PROBLEM_NO = 95
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
        3,
        # 1,
        # 2,
    ]
    for x in cases:
        ans = sol.generateTrees(x)
        for t in ans:
            print(TreeNode.tree_to_array(t))

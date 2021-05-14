import importlib.util
import inspect
import glob, os

PROBLEM_NO = 22
PROBLEM_LV = '/Medium/'

os.chdir(os.path.dirname(__file__))
file_path = glob.glob(os.getcwd() + PROBLEM_LV + str(PROBLEM_NO) + '.*.py')[0]
print(file_path)

spec = importlib.util.spec_from_file_location(os.path.basename(file_path), file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

cls = None
for member in inspect.getmembers(module):
    if member[0] == 'Solution':
        cls = member[1]

if __name__ == "__main__":
    sol = cls()
    print(sol.generateParenthesis(1))
    print(sol.generateParenthesis(2))
    print(sol.generateParenthesis(3))
    # print(sol.generateParenthesis(4))
    # print(sol.generateParenthesis(5))
    # print(sol.generateParenthesis(6))
    # print(sol.generateParenthesis(7))
    # print(sol.generateParenthesis(8))

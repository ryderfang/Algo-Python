import importlib.util
import inspect
import glob, os

PROBLEM_NO = 11
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
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
    print(sol.maxArea([1,1]))
    print(sol.maxArea([4,3,2,1,4]))
    print(sol.maxArea([1,2,1]))
    print(sol.maxArea([2, 1]))

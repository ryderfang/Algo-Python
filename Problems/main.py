import importlib.util
import inspect
import glob, os

PROBLEM_NO = 12
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
    print(sol.intToRoman(3))
    print(sol.intToRoman(4))
    print(sol.intToRoman(9))
    print(sol.intToRoman(58))
    print(sol.intToRoman(1994))
    print(sol.intToRoman(2998))

import importlib.util
import inspect
import os

os.chdir(os.path.dirname(__file__))
file_name = '8.string-to-integer-atoi'
spec = importlib.util.spec_from_file_location(file_name + '.py', os.getcwd() + '/Medium/' + file_name + '.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

cls = None
for member in inspect.getmembers(module):
    if member[0] == 'Solution':
        cls = member[1]

if __name__ == "__main__":
    sol = cls()
    print(sol.myAtoi("42"))
    print(sol.myAtoi("   -42"))
    print(sol.myAtoi("4193 with words"))
    print(sol.myAtoi("words and 987"))
    print(sol.myAtoi("-91283472332"))
    print(sol.myAtoi("91283472332"))
    print(sol.myAtoi("+-12"))

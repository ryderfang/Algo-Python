import importlib.util
import inspect
import os

os.chdir(os.path.dirname(__file__))
file_name = '6.zig-zag-conversion.py'
spec = importlib.util.spec_from_file_location(file_name, os.getcwd() + '/Medium/' + file_name)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

cls = None
for member in inspect.getmembers(module):
    if member[0] == 'Solution':
        cls = member[1]

if __name__ == "__main__":
    sol = cls()
    print(sol.convert("PAYPALISHIRING", 3))
    print(sol.convert("PAYPALISHIRING", 4))
    print(sol.convert("P", 2))

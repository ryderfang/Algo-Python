import importlib.util
import inspect

file_name = '3.longest-substring-without-repeating-characters.py'
spec = importlib.util.spec_from_file_location(file_name, 'Problems/Medium/' + file_name)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

cls = None
for member in inspect.getmembers(module):
    if member[0] == 'Solution':
        cls = member[1]

if __name__ == "__main__":
    sol = cls()
    print(sol.lengthOfLongestSubstring('abcabcbb'))

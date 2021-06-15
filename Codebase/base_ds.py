#! /usr/local/bin/python3

def test_compare():
    x = 3
    if 3 == x > 1:
        print("pass")
    if 1 <= x < 10:
        print("pass")

# singleton in python
class Singleton(object):
    def foo(self):
        pass
singleton = Singleton()

# 有时间了解下 pysnooper - debugger 神器

if __name__ == "__main__":
    test_compare()
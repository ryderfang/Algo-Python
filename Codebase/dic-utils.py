#! /usr/local/bin/python3

if __name__ == "__main__":
    dic = {'k1': 1, 'k2': 2}
    # instead for dic['k3'] without exception
    print(dic.get('k3', 0))

    # union
    a = {'a': 4, 'b': 2}
    b = {'a': 1, 'd': 6, 'b': 3}
    print({**a, **b})
    # py 3.9 support
    # print(a | b)

    pass
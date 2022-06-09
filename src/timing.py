import timeit

def func1(n):
    return [n for n in range(1, 100) if n % 2 == 0]


def func2(n):
    return [n for n in range(1, 200) if n % 2 == 0]


if __name__ == '__main__':
    setup = '''def func1(n):
        return [n for n in range(1, 100) if n % 2 == 0]'''
    statement = '''func1(100)'''
    print(timeit.timeit(statement, setup, number=10000))
    setup1 = '''def func2(n):
        return [n for n in range(1, 200) if n % 2 == 0]'''
    statement1 = '''func2(100)'''
    print(timeit.timeit(statement1, setup1, number = 10000))

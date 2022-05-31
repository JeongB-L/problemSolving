def ask():
    while True:
        try:
            given = int(input('please enter an integer: '))
        except:
            print('you did not enter an integer')
            continue
        else:
            print(f'the result is: {given ** 2}')
            break
        finally:
            print('done')

if __name__ == '__main__':
    try:
        for i in ['a', 'b', 'c']:
            print(i**2)
    except TypeError:
        print('not a number')

    finally:
        print('end of try and except')

    x = 5
    y = 0
    try:
        z = x / y
    except ZeroDivisionError:
        print('an error occurred')
    finally:
        print('all done')

    ask()


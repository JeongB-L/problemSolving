import random

#   Create a generator that generates the squares of numbers up to some number N.
def gensquares(n):
    for a in range(n):
        yield a**2

#   Create a generator that yields "n" random numbers between a low and high number (that are inputs).
# Note: Use the random library. For example:

def rand_num(low, high, n):
    for num in range(n):
        yield random.randint(low, high)


if __name__ == '__main__':
    for x in gensquares(10):
        pass
        #print(x)

    for num in rand_num(1, 10, 12):
        pass

    #   Use the iter() function to convert the string below into an iterator:

    s = 'hello'
    s_iter = iter(s)

    #   Explain a use case for a generator using a yield
    #   statement where you would not want to use a normal function with a return statement.

    #   Answer: The case that the yeild function being more preferred than return function is when
    #   there the memory efficiency is required for generating huge amount of data one by one

    my_list = [1, 2, 3, 4, 5]

    gencomp = (item for item in my_list if item > 3)

    for item in gencomp:
        print(item)

    #   for item in my_list:
        #   if item > 3:
            #   yield item


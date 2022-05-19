from random import shuffle

def shuffle_list(temp):
    shuffle(temp)
    return temp

def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input('Please choose a number between 0,1, and 2:  ')
    return int(guess)

def check_answer(temp, guess):
    if temp[guess] == '0':
        print('Correct choice')
    else:
        print('Wrong choice')

def say_hi():
    print('hola')
def even_checker(num):
    if num % 2 == 0:
        print("true")
        return True
    else:
        return False
def something_here(num_list):
    even_numbers = []
    for num in num_list:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            pass
    return even_numbers
  
  if __name__ == '__main__':

    for x in range(1, 101):
        result = ""
        a = True
        if x % 3 == 0:
            result = result + 'Fizz'
            a = False
        if x % 5 == 0:
            result = result + 'Buzz'
            b = False
        if a == True:
            result = x
        print(result)
        say_hi()
        le = even_checker(5)
        vo = something_here([1,2,3,4,5,6])
        print(f'{le} and {vo}')

def lesser_of_two_evens(a, b):
    lesser = 0
    greater = 0
    if a > b:
        lesser = b
        greater = a
    else:
        lesser = a
        greater = b
    if a % 2 == 0 and b % 2 == 0:
        return lesser
    else:
        return greater
def animal_crackers(text):
    a = text.split()
    if a[0][0] == a[1][0]:
        return True
    else:
        return False

def makes_twenty(n1, n2):
    if n1 + n2 == 20 or n1 == 20 or n2 == 20:
        return True
    else:
        return False

def old_macdonald(name):
    i = 0
    alpha = ''
    for a in name:
        if i == 0 or i == 3:
            alpha = alpha + a.upper()
        else:
            alpha = alpha + a
        i = i + 1
    return alpha
# or
# first_letter = name[0].upper()
# inbetween = name[1:3]
# fourth_letter = name[3].upper()
# rest = name[4:]
# return first_letter + inbetween + fourth_letter + rest

def master_yoda(sentence):
    input = sentence.split()
    input = input[::-1]
    a = " ".join(input)
    return a

def almost_there(n):
    if 90 <= n <= 110 or 190 <= n <= 210:
        return True
    else:
        return False

def has_33(nums):
    #flag = False
   #i = 0
   # length = len(nums)
    #for num in nums:
        #if i == length - 1:
         #   break
       # if num == 3 and nums[i + 1] == 3:
        #    flag = True
        #    break
      # i = i + 1
    #return flag;
    for i in range(0, len(nums) - 10):
        if nums[i:i+2] == [3,3]:
            return True
    return False

def paper_doll(text):
    result = ''
    for t in text:
        result = result + t * 3
    return result

def BlackJack(a, b, c):
    summation = a + b + c
    if summation <= 21:
        return summation
    if summation > 21:
        if a == 11 or b == 11 or c == 11:
            summation = summation - 10
    if summation > 21:
        return 'BUST'
    else:
        return summation
def BlackJack1(a, b, c):
    su = sum([a,b,c])
    if su <= 21:
        return su
    elif 11 in [a, b, c] and su <= 21:
        return su - 10
    else:
        return 'BUST '

def summer_69(arr):
    result = 0
    flag = True
    for a in arr:
        if a == 6:
            flag = False
        if flag == True:
            result = result + a
        if flag == False and a == 9:
            flag = True
    return result

def spy_game(nums):
    flag = False
    i = 0
    j = 0
    length = len(nums)
    for num in nums:
        if i == length - 2:
            break
        if num == 0:
            j = i
            for num1 in nums[i + 1::]:
                j = j + 1
                if num1 == 0:
                    for num2 in nums[j + 1::]:
                        if num2 == 7:
                            flag = True
            break
        i = i + 1
    return flag

def spy_game_better_version(nums):
    #   do not forget this method of problem solving
    #   [0, 7, 'x']
    #   [7, 'x']
    #   ['x']
    given_code = [0, 0, 7, 'x']
    for num in nums:
        if num == given_code[0]:
            given_code.pop()
            #   pops whenever the num matches to the given code in an order.
            #   returns the boolean value whether x is the only remaining element of the code
    return len(given_code) == 1

def count_primes(num):
    counter = 0
    flag = True
    for n in range(2, num):
        #   use a nested for loop to check if there is any other number that can divide n besides 1 and itself
        for n1 in range(2, n):
            if n % n1 == 0:
                flag = False
                #   check if the current n is a prime number or not
                break
                #   breaks the loop right after the proof of n not being a prime number is discovered
            else:
                flag = True
                # maintaining the flag's value as True as long as it is not a prime number
        if flag == True:
            counter = counter + 1
    return counter

def count_primes2(num):
    if num < 2:
        return 0
    primes = [2]
    #   store 2 because it is a prime number
    x = 3
    while x <= num:
        for y in range(3, x, 2):
            #   check every number by two after 3, which is checking all the odd numbers because no even number is a prime number
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    return len(primes)


def print_big(letter):
    dic = {'a': '  *\n * *\n*****\n*   *\n*   *'}
    print(dic[letter])

if __name__ == '__main__':
    print(lesser_of_two_evens(4, 8))
    print(animal_crackers('gay gome'))
    print(makes_twenty(4, 6))
    print(old_macdonald('macdonald'))
    print(master_yoda('you are vewy nice'))
    print(almost_there(91))
    print(has_33([3,1,3]))
    print(paper_doll('Mississippi'))
    print(BlackJack(9,9,11))
    print(summer_69([2,1,6,9,11]))
    print(spy_game([1,7,2,0,4,5,0]))
    print(count_primes(100))
    print_big('a')

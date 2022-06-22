def hex_and_binary(n):
    return f'hexadecimal: {hex(n)}, binary: {bin(n)}'
if '__main__' == __name__:
    #   1. convert 1024 to binary and hexadecimal representation
    print(hex_and_binary(1024))
    #   2. round 5.23222 to two decimal places
    print(round(5.23222))
    #   3. check if every letter in the string s is lower case
    s = 'hello how are you Mary, are you feeling okay?'
    print(s.isupper())
    #   4. how many times does the letter 'w' show up in the string below?
    s1 = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
    print(s1.count('w'))
    #   5. find the elements in set1 that are not in set2
    set1 = {2, 3, 1, 5, 6, 8}
    set2 = {3, 1, 7, 5, 6, 8}
    set1.difference_update(set2)
    print(set1)
    #   6. find all elements that are in either set:
    set1 = {2, 3, 1, 5, 6, 8}
    set2 = {3, 1, 7, 5, 6, 8}
    set1.intersection_update(set2)
    print(set1)
    #   7. create this dictionary: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64} using a dictionary comprehension
    dic = {a: a**3 for a in range(5)}
    print(dic)
    #   8. reverse the list below:
    list1 = [1, 2, 3, 4]
    list1.reverse()
    print(list1)
    #   9. sort the list below:
    list2 = [3, 4, 2, 5, 1]
    list2.sort()
    print(list2)


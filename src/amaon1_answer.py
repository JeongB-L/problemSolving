#   Given an array of integers nums and an integer target, return values of the two numbers such that they add up to the target
#   You may assume that each input would have exactly one solution, and you may not use the same element twice
#   You can return the answer in any order

def getSum(nums, target):

    visitedSet = list()

    for num in nums:

        if target - num in visitedSet:

            return [num, target - num]

        else:

            visitedSet.append(num)

    return [-1]

if __name__ == '__main__':
    temp_list = [2, 7, 15]
    target = 26
    print(getSum(temp_list, target))
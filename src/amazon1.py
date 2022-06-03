#   Given an array of integers nums and an integer target, return values of the two numbers such that they add up to the target
#   You may assume that each input would have exactly one solution, and you may not use the same element twice
#   You can return the answer in any order
def targetting(given_array, target):
    crr_value = 0
    crr_location = 0
    sum_list = []
    for element in given_array:
        #   the current element is stored in crr_value to keep track of summation
        crr_value = element
        for the_rest in given_array[crr_location + 1:]:
            if crr_value + the_rest == target:
                sum_list.append(crr_value)
                sum_list.append(the_rest)
                break
        crr_location += 1
    return sum_list


if __name__ == '__main__':
    temp_list = [2, 12, 11, 7, 15]
    target = 9
    print(targetting(temp_list, target))
    #   output should be 2, 7

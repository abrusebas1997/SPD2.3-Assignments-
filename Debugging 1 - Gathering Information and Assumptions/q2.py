def contains_3_consecutive(list_of_nums):
    """Return True if the list contains 3 consecutive 
       numbers each increasing by 1.
    """
    for i in range(len(list_of_nums) - 2):
        list_of_nums.sort()
        if (list_of_nums[i+1] == list_of_nums[i] + 1 and
            list_of_nums[i+2] == list_of_nums[i] + 2):
            return True
        else:
            return False

    return False

if __name__ == '__main__':
    print('### Consecutive Numbers ###')
    answer1 = contains_3_consecutive([1, 2, 4])
    print(answer1) # should print False

    answer2 = contains_3_consecutive([4, 1, 2, 3])
    print(answer2) # should print True
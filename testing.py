# def find_largest_number(list_of_nums):
#  largest_num = list_of_nums[0]
#  for i in range(0, len(list_of_nums)):
#    if list_of_nums[i] > largest_num:
#      largest_num = list_of_nums[i]
#  return largest_num

# answer = find_largest_number([3, 2, 1, 5, 4])
# print(answer)

# def get_largest_num(list_of_nums):
#    list_of_nums = list_of_nums.sort()
#    last_index = len(list_of_nums) - 1
#    return list_of_nums[last_index]

# print(get_largest_num([5, 2, 17, 8, 3]))

def find_largest_diff(list_of_nums):
    """Find the largest difference between *consecutive* 
       numbers in a list.
    """
    largest_diff = 0
    for i in range(0, len(list_of_nums)):
        diff = abs(list_of_nums[i] - list_of_nums[i+1])
        if diff > largest_diff:
            largest_diff = diff

    return largest_diff

if __name__ == '__main__':
    print('### Largest Difference ###')
    answer = find_largest_diff([5, 3, 1, 2, 6, 4])
    print(answer)
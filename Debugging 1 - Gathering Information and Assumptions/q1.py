def find_largest_diff(list_of_nums):
    """Find the largest difference between *consecutive* 
       numbers in a list.
    """
    largest_diff = 0
    for i in range(len(list_of_nums) - 1):
        diff = abs(list_of_nums[i] - list_of_nums[i+1])
        if diff > largest_diff:
            largest_diff = diff

    return largest_diff

if __name__ == '__main__':
    print('### Largest Difference ###')
    answer = find_largest_diff([5, 3, 1, 2, 6, 4])
    print(answer)

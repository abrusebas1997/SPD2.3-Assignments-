def binary_search(arr, element, low=0, high=None):
    """Returns the index of the given element within the array by performing a binary search. """
    if high == None:
        high = len(arr) - 1

    if high < low:
        return -1

    mid = (high + low) // 2

    if arr[mid] == element:
        return mid

    elif arr[mid] > element:
        return binary_search(arr, element, low, mid-1)

    else:
        return binary_search(arr, element, mid+1, high)


if __name__ == '__main__':
    print('### Binary Sort ###')
    answer = binary_search([1, 2, 4, 5, 7], 7)
    print(answer)


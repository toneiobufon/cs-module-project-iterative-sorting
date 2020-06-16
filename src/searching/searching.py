def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1 # in this case the array is empty
    # Your code here
    low = 0
    high = len(arr)-1

    
    while low < high:
        mid = (low + high) // 2 # dividing by // eliminates fractions

        if arr[mid] == target:
            return mid
        
        elif target < arr[mid]:
            high = mid

        else:
            low = mid + 1


    return -1  # not found

def linear_search(arr, target):
    # Your code here


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    lo = 0
    hi = len(arr)

    #while lo and hi do not overlap
    while lo < hi:
        mid = (lo + hi) // 2 # dividing by // eliminates fractions

        if arr[mid] == target:
            return True
        
        elif target < arr[mid]:
            hi = mid

        else:
            lo = mid + 1


    return False  # not found

# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if end >= start:    # if there is a list of more than 1 sorted,
        mid = (start + end) // 2  # establish/set the middle point
        if arr[mid] == target:  # if the middle point IS the target, return it
            return mid
        # if the middle is higher than the target, shift the middle to the left (-1)
        elif arr[mid] > target:
            # recurse with new end being one less than the middle
            return binary_search(arr, target, start, mid - 1)
        else:
            # else recurse the other direction with the start being one plus
            return binary_search(arr, target, end, mid + 1)
    else:
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively


# def agnostic_binary_search(arr, target):
    # Your code here

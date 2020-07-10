import time

# 5, 9, 3, 7, 2, 8, 1, 6
# quick-sort algorithm
# 1) choose a pivot (any point in the array)
# take first number in list
# 2) move all elements smaller than pivot to the left of the pivot
# all elements larger than pivot move to the right
# 3) repeat steps through recursion on left and right side of initial pivot.


def partition(numbers):
    # this function breaks numbers into a left, pivot and right
    # divide, figure out how to properly split data
    left = []
    pivot = numbers[0]
    right = []
    # partition the numbers correctly
    for num in numbers[1:]:  # start on the second (non pivot)
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)

    return left, pivot, right


def quicksort(numbers):
    # base case
    # what is the easiest array to sort
    if len(numbers) <= 1:
        return numbers
    # partition the numbers
    left, pivot, right = partition(numbers)
    pivot = [pivot]  # make sure it's an array of size 1

    sorted_array = quicksort(left) + pivot + quicksort(right)
    return sorted_array


print(quicksort([5, 9, 3, 7, 2, 8, 1, 6]))

# O(nLog(n))      RESEARCH THIS RESEARCH THIS RESEARCH THIS

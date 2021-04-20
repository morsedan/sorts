# Quick Sort Steps
# Choose a pivot
# Create new array with pivot as only element
# Create an array of elements less than pivot on the left
# Create an array of elements greater than pivot on the right
# Repeat with arrays on left and right
# Combine sorted arrays and return a single sorted array

def quicksort(numbers):  # perfect: O(n log n)  worst: n^2
    # perfect: because it goes log(n) levels (dividing by two each time)
    # with n at each level (due to the partition) so doing n operations log(n) times
    # Assuming the array is pretty balanced (being split in half each time)

    # average: because you choose the smallest or biggest element each time
    # which means you are doing n operations n times (with no dividing each time)

    # base case (conquer)
    if len(numbers) <= 1:
        return numbers

    # recursive case (divide)
    left, pivot, right = partition(numbers)  # O(n)
    sorted_array = quicksort(left) + pivot + quicksort(right)
    return sorted_array


def partition(numbers):  # Runs in O(n)
    # helper function to split array into left, pivot, and right
    left = []
    pivot = [numbers[0]]
    right = []

    for num in numbers[1:]:  # Starting at index of 1 to skip pivot
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)

    return left, pivot, right


# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    current_index = 0
    while len(arrA) >= 1 or len(arrB) >= 1:
        if arrA and arrB:
            if arrA[0] > arrB[0]:
                merged_arr[current_index] = arrB.pop(0)
            else:
                merged_arr[current_index] = arrA.pop(0)
        elif arrB:
            merged_arr[current_index] = arrB.pop(0)
        else:
            merged_arr[current_index] = arrA.pop(0)
        current_index += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    return arr

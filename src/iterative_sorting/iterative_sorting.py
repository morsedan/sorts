# O(n) linear time
def linear_search(arr, target):
    for num in arr:
        if num == target:
            return True
        return False

# O(log(n)) logarithmic
def binary_search(arr, target):
    start = 0
    end = (len(arr) - 1)
    found = False

    while end >= start and not found:
        # find middle point
        middle_index = (start + end) // 2

        # compare mid-value with target
        # if the middle value is the same as target then we found it
        if arr[middle_index] == target:
            found = True

        # move start or end index closer to one another (narrow down the possible range)
        else:
            if arr[middle_index] > target:
                # target is smaller so search the left hand side
                end = middle_index - 1
            else:
                # target is larger so search the right hand side
                start = middle_index + 1
    return found

# O(n^2)
def insertion_sort(list_to_sort):
    # first element is already on the "sorted side"
    # all other elements need to be examined

    # iterate through the array starting at index 1 and going to end
    for i in range(1, len(list_to_sort) - 1):
        # number at the current index is being sorted
        current_num = list_to_sort[i]
        # keep track of where the current number is while we move it
        j = i
        # while it is bigger than the one on the left OR is at the beginning of the array
        while j > 0 and current_num < list_to_sort[j - 1]:
            # move the bigger number to the right
            list_to_sort[j] = list_to_sort[j - 1]
            # update the index of where the current number is
            j -= 1
        # put the current number at the index we found that it should be in
        list_to_sort[j] = current_num



# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             



        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
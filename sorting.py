#Sorting

def bubble_sort(lst):
    """Returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap.

        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """

    for j in range(len(lst)-1):
        made_swap = False
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                made_swap = True
        if not made_swap:
            break
    return lst


def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list
    containing all integers in the input lists.

    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    final_list = []
    left_index = 0
    right_index = 0

    while left_index < len(list1) and right_index < len(list2):
        if list1[left_index] < list2[right_index]:
            final_list.append(list1[left_index])
            left_index += 1
        else:
            final_list.append(list2[right_index])
            right_index += 1

    if left_index >= len(list1):
        final_list.extend(list2[right_index:])
    if right_index >= len(list2):
        final_list.extend(list1[left_index:])

    return final_list


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.

    Finish the merge sort algorithm by writing another function that takes in a
    single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all
    integers from the input list. In other words, the new function should sort
    a list using merge_lists and recursion.

    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """

    if len(lst) <= 1:
        return lst

    half = len(lst) // 2
    left = lst[:half]
    right = lst[half:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_lists(left, right)


#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print

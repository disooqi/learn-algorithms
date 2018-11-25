

unsorted_array = [5, 1, 3, 0, 7, 9, 3]

key = 0 # index of current element in the list
while key < len(unsorted_array):
    i = key-1
    # Note that the and-operator in the test must use short-circuit evaluation, otherwise the test might get stuck with
    # an array bounds error
    while i >=0 and unsorted_array[i+1] < unsorted_array[i]:
        tmp = unsorted_array[i]
        unsorted_array[i] = unsorted_array[i+1]
        unsorted_array[i+1] = tmp

        i -= 1
    else:
        print(unsorted_array)

    key += 1

#######################################################################
print('-'*80)
#######################################################################

# Pythonic
# a slightly faster version can be produced that moves A[i] to its position in one go and only performs one assignment
# in the inner loop body






######################################################################
def insertion_sort(ulist):
    """

    The best case input is an array that is already sorted. In this case insertion sort has a linear running time (i.e.,
    O(n)). During each iteration, the first remaining element of the input is only compared with the right-most element
    of the sorted subsection of the array.
    The simplest worst case input is an array sorted in reverse order. The set of all worst case inputs consists of all
    arrays where each element is the smallest or second-smallest of the elements before it. In these cases every
    iteration of the inner loop will scan and shift the entire sorted subsection of the array before inserting the next
    element. This gives insertion sort a quadratic running time (i.e., O(n2)).
    The average case is also quadratic[5], which makes insertion sort impractical for sorting large arrays. However,
    insertion sort is one of the fastest algorithms for sorting very small arrays, even faster than quicksort; indeed,
    good quicksort implementations use insertion sort for arrays smaller than a certain threshold, also when arising as
    subproblems; the exact threshold must be determined experimentally and depends on the machine, but is commonly
    around ten.
    Example: The following table shows the steps for sorting the sequence {3, 7, 4, 9, 5, 2, 6, 1}. In each step, the
    key under consideration is underlined. The key that was moved (or left in place because it was biggest yet
    considered) in the previous step is marked with an asterisk.
    :param ulist:
    :return:
    """
    for key, element in enumerate(ulist):
        i = key - 1
        while i >= 0 and element < ulist[i]:  # (i+1) is the key index
            ulist[i + 1] = ulist[i]
            i -= 1
        else:
            ulist[i + 1] = element
            # print(ulist)


if __name__ == '__main__':
    unsorted_list = [5, 1, 3, 0, 7, 9, 3]
    insertion_sort(unsorted_list)
    print()
    print(unsorted_list)


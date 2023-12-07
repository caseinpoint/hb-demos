"""This merge sort is written for ease of understanding. A slightly more
efficient implementation -- still O(n log n) though -- is implemented 
in sorts.py."""

from collections import deque

def merge_sort(lst):
    """Merge sort list and return result."""

    # Break everything down into a list of one (or less)
    if len(lst) < 2:
        return lst

    mid = int(len(lst) / 2)

    lst1 = merge_sort(lst[:mid])
    lst2 = merge_sort(lst[mid:])

    return make_merge(lst1, lst2)


def make_merge(lst1, lst2):
    """Merge lists."""

    result_list = []

    deq1 = deque(lst1)  # use deque so pop from beginning is fast
    deq2 = deque(lst2)

    while len(deq1) > 0 or len(deq2) > 0:
        # Handle case where one deque is empty
        if not deq1:
            result_list.append(deq2.popleft())
        elif not deq2:
            result_list.append(deq1.popleft())

        # Compare first element from each,
        # add smallest one to result_list
        elif deq1[0] < deq2[0]:
            result_list.append(deq1.popleft())
        else:
            result_list.append(deq2.popleft())

    return result_list


if __name__ == "__main__":
    print(merge_sort([2, 7, 1, 4]))

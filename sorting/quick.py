"""This quick sort is written for ease of understanding. A more
efficient implementation is used in sorts.py."""


def quicksort(lst):
    """Quicksort list and return result."""

    if len(lst) < 2:
        return lst

    # Select pivot element
    mid = int(len(lst) / 2)
    pivot = lst[mid]

    # Partition elements into buckets
    lo, hi, eq = [], [], []
    for elem in lst:
        if elem < pivot:
            lo.append(elem)
        elif elem == pivot:
            eq.append(elem)
        else:  # elem > pivot
            hi.append(elem)

    return quicksort(lo) + eq + quicksort(hi)

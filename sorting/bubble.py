def bubble_up(lst):
    """Bubble the highest number to the end"""

    for j in range(len(lst) - 1):

        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]


def bubble_sort(lst):
    """Basic bubble sort."""

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                # Pair out-of-order, swap them
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def shorter_bubble_sort(lst):
    """Shorter bubble sort."""

    for i in range(len(lst) - 1):
        # don't re-check already-sorted
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                # Pair out-of-order, swap them
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    # or, move the outer loop backwards
    # for i in range(len(lst) - 1, -1, -1):
        # stop the inner loop before i, that index has already been checked
        # for j in range(i):
        #     if lst[j] > lst[j + 1]:
        #         lst[j], lst[j + 1] = lst[j + 1], lst[j]


def best_bubble_sort(lst):
    """Shorter and fast-win bubble sort."""

    for i in range(len(lst) - 1):
        # keep track of whether we made a swap
        made_swap = False
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                made_swap = True
        if not made_swap:
            # If no swap, list already sorted
            break

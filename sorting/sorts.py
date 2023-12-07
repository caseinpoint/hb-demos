"""Demonstrate Python sorting functions."""


def display_list_idx(lst, i, j, r=False):
    """Print a list and relative positions of i and j.

    (up to 3-digit numbers)"""

    print("[", end="")
    for idx in range(len(lst) - 1):
        print(f"{lst[idx]:3.0f},", end="")
    print(f"{lst[-1]:3.0f}]")

    if not r:
        print(f"{' '*(4*i+3)}^{' '*(4*(j-i-1)+3)}^")
        print(f"{' '*(4*i+3)}i{' '*(4*(j-i)-1)}j")
    else:
        print(f"{' '*(4*j+3)}^{' '*(4*(i-j-1)+3)}^")
        print(f"{' '*(4*j+3)}j{' '*(4*(i-j)-1)}i")
    print()


def bubble_sort(lst, v=False):
    """Basic bubble sort.

    Loop & check side-by-side pair; swap if out of order.

    Runtime: O(n^2)
    """

    if v:
        print(f"starting lst: {lst}\n")
        count = 0

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                # Pair is out-of-order, swap them
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            if v:
                display_list_idx(lst, i, j)
                count += 1

    if v:
        print(f"final lst: {lst}\niterations: {count}")
# This version is non-optimized at all; it checks every pair,
# even if they're already in the right place.


def shorter_bubble_sort(lst, v=False):
    """Shorter bubble sort.

    Loop & check side-by-side pair; swap if out of order.

    Adds optimization: inner loop doesn't recheck end of list,
    as those numbers are already in the correct place. Reduces
    number of loops by half to `n*(n-1)`.

    Runtime: still O(n^2)
    """

    if v:
        print(f"starting lst: {lst}\n")
        count = 0

    for i in range(len(lst) - 1):
        # Next line changed: don't re-check already-sorted
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                # Pair is out-of-order, swap them
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            if v:
                display_list_idx(lst, i, j)
                count += 1

    if v:
        print(f"final lst: {lst}\niterations: {count}")


def shorter_bubble_rev(lst, v=False):
    """Shorter bubble sort, different approach.

    Loop & check side-by-side pair; swap if out of order.

    Adds optimization: inner loop doesn't recheck end of list,
    as those numbers are already in the correct place. Reduces
    number of loops by half to `n*(n-1)`.

    Runtime: still O(n^2)
    """

    if v:
        print(f"starting lst: {lst}\n")
        count = 0

    # Outer loop goes backwards
    for i in range(len(lst) - 1, 0, -1):
        # Next line changed: don't re-check already-sorted
        for j in range(i):
            if lst[j] > lst[j + 1]:
                # Pair is out-of-order, swap them
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            if v:
                display_list_idx(lst, i, j, True)
                count += 1

    if v:
        print(f"final lst: {lst}\niterations: {count}")


def best_bubble_sort(lst, v=False):
    """Best bubble sort.

    Loop & check side-by-side pair; swap if out of order.

    Adds "shorter" optimzation, above, and also an
    optimization that it stops the outer loop once the
    list is correctly sorted.

    This makes a huge difference for already-sorted input,
    as it now does `n`, not `n*(n-1)` looos. For
    reversed input (the pathologiclly worst case), still
    does `n*(n-1)` loops. For "average random" input,
    this saves about 10% over the worst case.

    Runtime: still O(n^2)
    """

    # Note: you'll see that in the random and reversed lists, this function
    # actually performs worse than shorter_bubble_sort() . There is a small
    # but tangible cost to using made_swap in this function that slows it down
    # when it would otherwise perform the same number of loops as
    # shorter_bubble_sort() .

    if v:
        print(f"starting lst: {lst}\n")
        count = 0

    for i in range(len(lst) - 1):
        # New optimization: keep track of whether we made a swap
        made_swap = False
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                made_swap = True
            if v:
                display_list_idx(lst, i, j)
                count += 1
        if not made_swap:
            # If nothing swapped, list is already sorted
            break

    if v:
        print(f"final lst: {lst}\niterations: {count}")


################################################################


def selection_sort(lst):
    """Selection sort.

    Go through list and move highest item to end each time.
    This is better than bubble sort, as it doesn't swap every
    pair, but moves only highest up each time --- so slightly
    more efficient.

    Runtime: O(n^2)
    """

    for i in range(len(lst)):
        high = None
        # Loop through the as-yet-unsorted part
        for j in range(len(lst) - i):
            if high is None or lst[high] < lst[j]:
                # Found the new highest element in this pass
                high = j
        # Swap highest element to right before sorted part
        lst[high], lst[j] = lst[j], lst[high]


################################################################


def insertion_sort(lst):
    """Insertion sort.

    Maintain sorted sublist at start; insert items from list
    into proper place in sorted sublist.

    Runtime: O(n^2)
    """

    # Loop over as-yet-unsorted part
    for i in range(1, len(lst)):
        # Get first unsorted value and remember where it was
        val = lst[i]
        j = i

        # Scan sorted (starting at higher-end) and scoot
        # everything forward until we find the "right" place
        # for this element
        while j >= 1 and val < lst[j - 1]:
            lst[j] = lst[j - 1]
            j -= 1

        # Put it in the right place
        lst[j] = val


def shell_sort(lst):
    """Shell sort, an improvement on insertion sort.

    Iteratively do insertion sorts, spread out across list.
    Does this iteratively over severl slices.

    Runtime: O(n^2)   (but often super-fast!)
    """

    # NOTE FROM JOEL: if you study one thing here, I'd make it
    # shell sort -- it's 95% the same as insertion sort,
    # except that it does it iteratively, in pieces. This makes
    # it ~100x faster for a large list, and it's a great
    # example of good algorithm design. While being
    # technically O(n^2), for lists <10,000, it will often
    # perform similarly to O(n log n) sorts, like
    # mergesort/quicksort.

    gap = len(lst) // 2

    while gap:
        for start in range(gap):

            # Insertion sort on lst, by gap, starting at start

            for i in range(start + gap, len(lst), gap):
                val = lst[i]
                j = i

                while j >= gap and val < lst[j - gap]:
                    lst[j] = lst[j - gap]
                    j -= gap

                lst[j] = val

        gap //= 2


################################################################


def merge_sort(lst):
    """Merge sort.

    Divide and conquer: reduce to lists of 0-1 items, then recombine.

    Runtime: O(n log n)
    """

    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        # merge-lecture-snippet-start
        left_index = right_index = new_index = 0

        # Interleave left and right into list

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                lst[new_index] = left[left_index]
                left_index += 1
            else:
                lst[new_index] = right[right_index]
                right_index += 1
            new_index += 1
        # merge-lecture-snippet-end

        # If lists were uneven length, add remainder of longer list

        while left_index < len(left):
            lst[new_index] = left[left_index]
            left_index += 1
            new_index += 1

        while right_index < len(right):
            lst[new_index] = right[right_index]
            right_index += 1
            new_index += 1


def quicksort(lst):
    """Quicksort.

    Iteratively pivot, sort lists, and combine.

    Runtime: O(n log n)
    """

    import random

    def _quicksort(lst, first, last):
        if first < last:

            # Find pivot point

            pivot = first + random.randrange(last - first + 1)
            lst[pivot], lst[last] = lst[last], lst[pivot]

            pivot = first

            for i in range(pivot, last):
                if lst[i] <= lst[last]:
                    lst[i], lst[pivot] = lst[pivot], lst[i]
                    pivot += 1

            lst[pivot], lst[last] = lst[last], lst[pivot]

            # Recurse
            _quicksort(lst, first, pivot - 1)
            _quicksort(lst, pivot + 1, last)

    _quicksort(lst, 0, len(lst) - 1)


def counting_sort(lst):
    """Non-comparative sort for integers. Super-fast if keys are similar to
    size."""

    # NOTE FROM JOEL: this sort, as written, only makes sense if we know that
    # our input are positive numbers, in the range 0..k, where k is the length
    # of the list. As we know that, we can write a sort that performs in O(n)
    # time -- faster than the limit of O(n log n) for comparative sorts.

    counter = [0] * (len(lst) + 1)

    for i in lst:
        counter[i] += 1

    ndx = 0
    for i in range(len(counter)):
        while counter[i]:
            lst[ndx] = i
            ndx += 1
            counter[i] -= 1


def heap_sort(lst):
    """Add items to binary heap (keeping them in order!) and then extract."""

    def move_down(first, last):
        """Move item down in heap to proper place."""

        # Assume left-hand child is bigger
        largest = 2 * first + 1

        while largest <= last:
            if largest < last and lst[largest] < lst[largest + 1]:
                # Right child exists and is larger than left child
                largest += 1

            if lst[largest] > lst[first]:
                # Selected child is bigger than parent, so swap
                lst[largest], lst[first] = lst[first], lst[largest]

                # Move down to largest child
                first = largest
                largest = 2 * first + 1

            else:
                # Once we don't swap, it's in the right place; exit
                return

    # Convert lst to heap

    length = len(lst) - 1
    least_parent = length // 2

    for i in range(least_parent, -1, -1):
        move_down(i, length)

    # Flatten heap into sorted array

    for i in range(length, 0, -1):
        if lst[0] > lst[i]:
            lst[0], lst[i] = lst[i], lst[0]
            move_down(0, i - 1)


def timsort(lst):
    """Python's built-in sort, timsort: a combination of
    merge_sort/insertion_sort.

    Generally, a very fast algorithm, but also will be much faster than the
    others because it's written in C.
    """

    lst.sort()


def balloonicorn_sort(lst):
    """Not a sort -- cheats and just recreates initial range!"""

    # Here basically just to show how fast timsort is -- it's almost as fast
    # to run that, written in C, as it is just to cheat and re-create an
    # already-sorted list.

    lst[:] = range(len(lst))


if __name__ == '__main__':
    import random
    import time
    import sys

    def _almost(lst):
        """Changes list to "mostly" sorted -- ~10% of elements are
        slightly-out-of-place."""

        lst.sort()
        for i in range(len(lst) // 20):
            x = random.randint(0, len(lst) - 6)
            y = x + random.randint(1, 5)
            lst[x], lst[y] = lst[y], lst[x]

    def _almost_rev(lst):
        """Changes list to "mostly" sorted -- ~10% of elements are
        slightly-out-of-place."""

        _almost(lst)
        lst.reverse()


    count = 3000  # length of lists to test with
    reps = range(3)  # number of times to repeat each sort

    if len(sys.argv) > 1:
        count = int(sys.argv[1])
    if len(sys.argv) > 2:
        reps = range(int(sys.argv[2]))

    # To get the best possible comparison of performance, let's pre-generate
    # the list(s) we're going to :

    # Map our 'types' of lists to the function that generates them:
    list_func_dict = {
        'random': random.shuffle,
        'sorted': lambda x: 0,
        'reversed': lambda x: x.reverse(),
        'almost': _almost,
        'almost_rev': _almost_rev,
    }

    # Generate dictionary of lists of lists so that each type has as many
    # lists to sort as we have reps:
    master_lsts = {}
    for list_type, list_func in list_func_dict.items():
        master_lsts[list_type] = []
        for i in reps:

            master_lsts[list_type].append(list(range(count)))
            list_func(master_lsts[list_type][-1])

    # Start sorting:
    print("Balloonicorn's Super Sort Examiner")
    print(f"Sorting of list of {count} items {len(reps)} times")
    print()
    print("sort                 random     sorted     rev        almost     almost_rev")

    for func in [
        bubble_sort,
        shorter_bubble_sort,
        best_bubble_sort,
        selection_sort,
        insertion_sort,
        shell_sort,
        merge_sort,
        quicksort,
        heap_sort,
        counting_sort,
        timsort,
        # balloonicorn_sort,
    ]:

        print(f"{func.__name__:21}", end='')

        # For each type of lists, go through the specified number of reps:
        for list_type in ['random', 'sorted', 'reversed', 'almost', 'almost_rev']:

            elapsed = 0
            for i in reps:
                # Make a copy of the list from our master lists:
                lst = master_lsts[list_type][i][:]

                start = time.time()

                # Do the actual sort
                func(lst)

                # Find out how long the actual sort took
                elapsed += (time.time() - start)
            assert lst == list(range(count))

            print(f"{elapsed:2.5f}    ", end='')

        print()

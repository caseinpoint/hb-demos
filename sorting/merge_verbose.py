"""This merge sort is written for ease of understanding. An implementation
with better runtime is implemented in sorts.py.

It contains extra print statements and indentation to help understand the
recursive calls and return values.
"""


def merge_sort_verbose(lst, level=0):
    """Merge sort list and return result."""

    _print(f"Starting merge_sort_verbose on {lst}", level)

    level += 1

    # Break everything down into a list of one
    if len(lst) < 2:  # if length of lst is 1, return lst
        _print(f"Returning {lst}", level)
        return lst

    mid = int(len(lst) / 2)  # index at half the list
    left_half = lst[:mid]
    _print(f"Left half of {lst}: {left_half}", level)
    # divide list in half
    sorted_left_half = merge_sort_verbose(left_half, level + 1)
    _print(
        f"Left half of {lst} finished: {left_half} -> {sorted_left_half}",
        level,
    )

    right_half = lst[mid:]
    _print(f"Right half of {lst}: {right_half}", level)
    # assign other half
    sorted_right_half = merge_sort_verbose(right_half, level + 1)
    _print(
        f"Right half of {lst} finished: {right_half} -> {sorted_right_half}",
        level,
    )

    merged_list = make_merge_verbose(
        sorted_left_half, sorted_right_half, level
    )

    level -= 1

    _print(
        f"Returning merge_sort_verbose on {lst}: {merged_list}",
        level,
    )

    return merged_list


def make_merge_verbose(lst1, lst2, level=0):
    """Merge lists."""
    orig_lst1 = lst1[:]
    orig_lst2 = lst2[:]
    _print(
        f"Starting make_merge_verbose on {lst1} and {lst2}", level
    )

    # Compare first items of each pair of lists & interleave
    result_list = []
    while len(lst1) > 0 or len(lst2) > 0:
        # if items left in both lists
        # compare first items of each list
        if lst1 == []:
            result_list.append(lst2.pop(0))
        elif lst2 == []:
            result_list.append(lst1.pop(0))
        elif lst1[0] < lst2[0]:
            # append and rm first item of lst1
            result_list.append(lst1.pop(0))
        else:
            # append and rm first item of lst2
            result_list.append(lst2.pop(0))

    _print(
        f"Returning make_merge_verbose on {orig_lst1} and {orig_lst2}: {result_list}",
        level,
    )
    return result_list


def _print(string, level=0):
    """Convenience method to print text with indentation."""

    prefix = "    " * level
    print(f"{prefix}{string}")


if __name__ == "__main__":
    print(
        f"Final result: {merge_sort_verbose([2, 1, 7, 4, 5, 3, 6, 8])}"
    )

"""This merge sort is written for ease of understanding. An implementation
with better runtime is implemented in sorts.py."""


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

    print(f"len(lst1): {len(lst1)}, len(lst2): {len(lst2)}")
    count = 0

    while len(lst1) > 0 or len(lst2) > 0:
        # Handle case where one list is empty
        if lst1 == []:
            result_list.append(lst2.pop(0))
        elif lst2 == []:
            result_list.append(lst1.pop(0))

        # Compare first element from each list,
        # add smallest one to result_list
        elif lst1[0] < lst2[0]:
            result_list.append(lst1.pop(0))
        else:
            result_list.append(lst2.pop(0))

        count += 1

    print(f"iterations: {count}\n")

    return result_list


if __name__ == "__main__":
    print(merge_sort([2, 1, 7, 4]))

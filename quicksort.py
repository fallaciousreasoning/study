def naive_quicksort(items):
    if len(items) <= 1:
        return items

    pivot = items[0]

    left = []
    right = []

    for item in items[1:]:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)

    return naive_quicksort(left) + [pivot] + naive_quicksort(right)


"""
    How an iteration of quicksort should work.

    3 5 4 1 2 # pivot = 3, i = 0, j = 4, increment_i
    ^       ^
    2 5 4 1 3 # pivot = 3, i = 1, j = 4, !increment_i
      ^     ^
    2 3 4 1 5 # pivot = 3, i = 1, j = 3, increment_i
      ^   ^
    2 1 4 3 5 # pivot = 3, i = 2, j = 3, !increment_i
        ^ ^
    2 1 3 4 5 ## i == j == 2
"""

def partition(items, left, right):
    pivot = items[left]
    i = left #index of pivot

    def swap(i, j):
        juggle = items[j]
        items[j] = items[i]
        items[i] = juggle

    increment_i = False
    i = left
    j = right

    while i < j:
        if items[j] < pivot and not increment_i:
            swap(i, j)
            increment_i = True

        elif items[i] >= pivot and increment_i:
            swap(i, j)
            increment_i = False

        if increment_i:
            i += 1
        else: j -= 1


    return i

def quicksort(items, left=0, right=None):
    if right is None:
        right=len(items) - 1

    if right < left:
        return

    p = partition(items, left, right)

    quicksort(items, left, p - 1)
    quicksort(items, p + 1, right)

    return items

print(quicksort([1,7,4,8,3,2]))
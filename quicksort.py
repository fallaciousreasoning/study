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
    3 5 4 1 2 # pivot = 3, i = 0, j = 4, increment_i
    ^       ^
    2 5 4 1 3 # pivot = 3, i = 1, j = 4, !increment_i
      ^     ^
    2 3 4 1 5 # pivot = 3, i = 1, j = 3, increment_i
      ^   ^
    2 1 4 3 5 # pivot = 3, i = 2, j = 3, !increment_i
        ^ ^
    2 1 3 4 5 

    ============

"""

def quicksort(items, left=0, right=None):
    if right is None:
        right=len(items)

    if right - left <= 1:
        return

    right -= 1

    i = left
    j = right

    print(left, right)

    increment_i = False

    pivot = items[i]

    while i < j:
        if increment_i:
            if items[i] < pivot:
                pass

            else:
                items[j] = items[i]
                increment_i = False

        else: 
            if pivot < items[j]:
                pass

            else:
                items[i] = items[j]
                increment_i = True

        if increment_i:
            i += 1
        else: j -= 1

    items[i if increment_i else j] = pivot

    quicksort(items, left, i)
    quicksort(items, j, right)
    
    return items

print(quicksort([3,5,4,1,2]))
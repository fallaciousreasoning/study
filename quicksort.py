def naive_quicksort(items):
    if len(items) == 1 or len(items) == 0:
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

print(naive_quicksort([1, 6, 3, 1, 9]))
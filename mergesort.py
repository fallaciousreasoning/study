def mergesort(items):
    if len(items) <= 1:
        return items

    middle = len(items) // 2
    left = mergesort(items[:middle])
    right = mergesort(items[middle:])

    results = []
    while left and right:
        if left[0] < right[0]:
            results.append(left.pop(0))
        else:
            results.append(right.pop(0))

    if left:
        results += left

    if right:
        results += right

    return results

print(mergesort([4, 8, 1, 3, 0, 2, 5, 9, 6, 7]))
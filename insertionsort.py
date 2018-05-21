def naive_insertionsort(items):
    result = []

    for item in items:
        inserted = False
        for i in range(len(result)):
            if result[i] > item:
                inserted = True
                result.insert(i, item)
                break

        if not inserted:
            result.append(item)


    return result

print(naive_insertionsort([1,6,3,2,9,5]))
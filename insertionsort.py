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

def insertionsort(items):
    def swap(i, j):
        juggle = items[i]
        items[i] = items[j]
        items[j] = juggle

    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] > items[j]:
                swap(i, j)

    return items

print(insertionsort([1,6,3,2,9,5]))
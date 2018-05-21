def binary_search(items, for_item, min=0, max=None):
    if max is None:
        max = len(items) - 1

    guess_index = (min + max) // 2
    guess = items[guess_index]

    if guess == for_item: return guess_index

    if guess < for_item:
        return binary_search(items, for_item, min, guess_index)

    if guess > for_item:
        return binary_search(items, guess_index, max)
import random
from quicksort import quicksort, naive_quicksort
from mergesort import mergesort
from heapsort import heapsort
from insertionsort import naive_insertionsort

def test(sort_algorithm):
    sizes = [i for i in range(50, 1000, 50)]

    for size in sizes:
        print(f"Testing with {size} items")
        items = list(range(size))
        random.shuffle(items)
        
        items = sort_algorithm(items)


        for i in range(size):
            if not i == items[i]:
                print("Items were not correctly sorted!")
                print("Expected:", list(range(i + 1)))
                print("Got     :", items[:i+1])
                break

test(naive_insertionsort)

from heap import Heap

def heapsort(items):
    heap = Heap(items[:])

    result = []
    while heap.items:
        result.append(heap.pop())

    return result
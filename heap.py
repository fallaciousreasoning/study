import math

class Heap:
    def __init__(self, items=None):
        self.items = items or []

        for i in reversed(range(len(self.items) - 1)):
            self.sift_down(i)

    def insert(self, item):
        self.items.append(item)
        self.sift_up(len(self.items) - 1)

    def peek(self):
        return self.items[0]

    def delete(self):
        self.items[0] = self.items[-1]
        self.items.pop()

        self.sift_down(0)

    def pop(self):
        min = self.peek()
        self.delete()

        return min

    def left_index(self, parent_index):
        return parent_index * 2 + 1

    def right_index(self, parent_index):
        return parent_index * 2 + 2

    def parent_index(self, child_index):
        return math.floor((child_index - 1) / 2)

    def parent(self, index):
        return self.items[self.parent_index(index)]

    def sift_up(self, index):
        while self.parent(index) > self.items[index]:
            parent_index = self.parent_index(index)
            self.swap(parent_index, index)

            index = parent_index
        
        self.sift_down(index)

    def sift_down(self, index):
        left_index = self.left_index(index)
        right_index = self.right_index(index)

        # If we don't have children, no need to do anything
        if left_index >= len(self.items):
            return

        # Find the minimum child (or the left child, if we don't have a right child)
        min_child_index = left_index if right_index >= len(self.items) or self.items[left_index] < self.items[right_index] else right_index

        if self.items[index] > self.items[min_child_index]:
            self.swap(index, min_child_index)
            self.sift_down(min_child_index)


    def swap(self, index_a, index_b):
        b = self.items[index_b]

        self.items[index_b] = self.items[index_a]
        self.items[index_a] = b

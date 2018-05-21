class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)

        at = self.find_parent(self.root, value)
        if value < at.value:
            at.left = Node(value)
        else:
            at.right = Node(value)

    def find_parent(self, parent, value):
        if value < parent.value:
            if not parent.left:
                return parent

            return self.find_parent(parent.left, value)

        else:
            if not parent.right:
                return parent

            return self.find_parent(parent.right, value)

    def contains(self, value, base=''):
        if base == '':
            base = self.root

        if base is None:
            return None

        if base.value == value:
            return base

        if value < base.value:
            return self.contains(value, base.left)
        
        if value > base.value:
            return self.contains(value, base.right)

if __name__ == '__main__':
    tree = BinaryTree()

    items = [7,1,9,0,30,100,10]
    for item in items:
        tree.insert(item)

    for item in items:
        print(tree.contains(item) is not None)

    not_in = [-1, 22, 77, 72, 4]
    for item in not_in:
        print(tree.contains(item) is not None)


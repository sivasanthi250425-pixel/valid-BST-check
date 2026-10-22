class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.data:
        root.left = insert(root.left, key)
    elif key > root.data:
        root.right = insert(root.right, key)

    return root


def is_bst(root, low=float('-inf'),
           high=float('inf')):
    if root is None:
        return True

    if not (low < root.data < high):
        return False

    return (is_bst(root.left, low, root.data)
            and
            is_bst(root.right, root.data, high))


# Test 1: Valid BST using insertion
root = None
keys = list(map(int, input("Enter keys for valid BST: ").split()))

for key in keys:
    root = insert(root, key)

print("First tree is BST:", is_bst(root))


# Test 2: Manually linked invalid tree
root2 = Node(40)
root2.left = Node(20)
root2.right = Node(60)
root2.left.right = Node(45)

print("Second tree is BST:", is_bst(root2))
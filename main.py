class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def right_rotate(y):
    x = y.left
    T3 = x.right

    x.right = y
    y.left = T3

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x

def insert(root, key):
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root


def tree_min(node):
    current = node
    while current.left:
        current = current.left
    return current.key


def tree_max(node):
    current = node
    while current.right:
        current = current.right
    return current.key


def tree_sum(node):
    if not node:
        return 0
    return node.key + tree_sum(node.left) + tree_sum(node.right)


tree = AVLNode(10)
tree = insert(tree, 30)
tree = insert(tree, 20)
tree = insert(tree, 5)
tree = insert(tree, 4)
tree = insert(tree, 7)
tree = insert(tree, 1)
tree = insert(tree, 100)


print(tree_min(tree)) # 1
print(tree_max(tree)) # 100
print(tree_sum(tree)) # 177
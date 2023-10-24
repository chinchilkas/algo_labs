class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binary_tree_diameter(tree: BinaryTree) -> int:
    def find_diameter(node):
        if not node:
            return 0

        left_diameter = find_diameter(node.left)
        right_diameter = find_diameter(node.right)

        left_depth = get_depth(node.left)
        right_depth = get_depth(node.right)

        diameter = max(left_diameter, right_diameter, left_depth + right_depth)

        return diameter

    def get_depth(node):
        if not node:
            return 0

        left_depth = get_depth(node.left)
        right_depth = get_depth(node.right)

        return max(left_depth, right_depth) + 1
    return find_diameter(tree)

def binary_tree_diameter_2(tree: BinaryTree):
    leaves = []
    

tree = BinaryTree(1,
    BinaryTree(3,
        BinaryTree(7,
            BinaryTree(8, BinaryTree(9)),
            None
            ),
        BinaryTree(4,
            None,
            BinaryTree(5)
            )
    ),
    # BinaryTree(2)
)

result = binary_tree_diameter(tree)
print(result)



class TreeNode:
     def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def maxDepth(root: TreeNode, direction="root") -> int:
    if root is None:
        return 0

    currentNode = root.value
    # Print whether it's the left or right subtree (or the root)
    print(f"In {direction} subtree at node: {currentNode}")

    # Recursively calculate the depth of left and right subtrees
    left_depth = maxDepth(root.left, "left")
    right_depth = maxDepth(root.right, "right")

    return 1 + max(left_depth, right_depth)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.right = TreeNode(8)

# Call the maxDepth function
print(maxDepth(root), "max")  # Expected output: 4
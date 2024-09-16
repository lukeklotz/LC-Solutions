
class TreeNode:
     def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def goodNodes(root: TreeNode) -> int:

        def counter(node, maxVal):

            if node is None:
                return 0
            
            good = 0

            if node.val >= maxVal:
                good = 1
            else:
                good = 0

            maxVal = max(node.val, maxVal)

            good += counter(node.left, maxVal)
            good += counter(node.right, maxVal)

            return good

        return counter(root, root.val)


root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.right = TreeNode(8)

print(goodNodes(root))    
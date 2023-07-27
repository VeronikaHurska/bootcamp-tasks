class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder_recursive(node, result):
            if node is not None:
                inorder_recursive(node.left, result)
                result.append(node.val)
                inorder_recursive(node.right, result)
        
        
        result = []
        inorder_recursive(root, result)
        
        return result

root = TreeNode(4)
root.left = TreeNode(5)
root.right = TreeNode(82)
root.right.right = TreeNode(9)
root.right.right.right = TreeNode(2)

solution = Solution()
inorder_result = solution.inorderTraversal(root)
print(inorder_result) # 5 4 82 9 2 

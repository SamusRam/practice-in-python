class Solution:
    def __init__(self):
        self.max_val = -float('inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum(root)
        return self.max_val

    def max_path_sum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_max_sum = max(0, self.max_path_sum(root.left))
        right_max_sum = max(0, self.max_path_sum(root.right))
        self.max_val = max(self.max_val, left_max_sum + root.val + right_max_sum)
        return root.val + max(left_max_sum, right_max_sum)
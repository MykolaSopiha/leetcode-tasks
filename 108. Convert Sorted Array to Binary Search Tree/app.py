from typing import List, Optional

from data_structures import BinaryTreeNode as TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0: return None
        middle_index = int(len(nums) / 2)
        middle = nums[middle_index]
        return TreeNode(
            middle,
            self.sortedArrayToBST(nums[:middle_index]),
            self.sortedArrayToBST(nums[middle_index + 1:]),
        )

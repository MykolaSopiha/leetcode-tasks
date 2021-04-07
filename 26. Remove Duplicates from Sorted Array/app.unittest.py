import unittest

from app import Solution

class TestRemoveDuplicatesFromSortedArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_remove_duplicates(self):
        nums = [1,1,2]
        self.assertEqual(self.solution.removeDuplicates(nums), 2)
        self.assertEqual(nums, [1,2])

        nums = [0,0,1,1,1,2,2,3,3,4]
        self.assertEqual(self.solution.removeDuplicates(nums),  5)
        self.assertEqual(nums, [0,1,2,3,4])

if __name__ == '__main__':
    unittest.main()
import unittest

from app import Solution
from data_structures import compare_lists, create_list_node


class TestRemoveLinkedListElements(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_remove_elements(self):
        self.assertTrue(
            compare_lists(
                self.solution.removeElements(
                    create_list_node([1, 2, 6, 3, 4, 5, 6]),
                    6
                ),
                create_list_node([1, 2, 3, 4, 5])
            )
        )

        self.assertTrue(
            compare_lists(
                self.solution.removeElements(
                    create_list_node([1, 2, 6, 3, 4, 5, 6]),
                    1
                ),
                create_list_node([2, 6, 3, 4, 5, 6])
            )
        )

        self.assertTrue(
            compare_lists(
                self.solution.removeElements(
                    create_list_node([7, 7, 7, 7, 7, 7, 7, 7]),
                    7
                ),
                create_list_node([])
            )
        )

if __name__ == '__main__':
    unittest.main()

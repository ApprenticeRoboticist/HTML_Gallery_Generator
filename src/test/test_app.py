import unittest
import random

from src.app import delete_value


class TestListOperations(unittest.TestCase):
    def test_delete_value(self):
        example_list = []
        for x in range(15):
            x = random.randint(1, 100)
            example_list.append(x)

        delete_value(example_list)
        y = len(example_list)

        self.assertEqual(y, 14)


if __name__ == 'main':
    unittest.main()

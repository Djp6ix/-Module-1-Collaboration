import unittest

class TestSum(unittest.TestCase):

    def test_sum_list(self):
        result = sum([1, 2, 3])
        self.assertEqual(result, 6)

    def test_sum_tuple(self):
        result = sum((1, 2, 2))
        self.assertEqual(result, 6)

if __name__ == "__main__":
    unittest.main()

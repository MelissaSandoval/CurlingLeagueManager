import unittest
from module6.exercises.iterators import OddIterator, Last


class TestOddIterator(unittest.TestCase):
    def test_odd_iterator(self):
        odd_iter = OddIterator([2, 3, 7, 6, 12, 19])
        self.assertEqual(next(odd_iter), 3)
        self.assertEqual(next(odd_iter), 7)
        self.assertEqual(next(odd_iter), 19)


class TestLast(unittest.TestCase):
    def test_last(self):
        last_iter = Last([1, 2, 3, 4, 5, 6, 7, 8], 3)
        self.assertEqual(next(last_iter), 6)
        self.assertEqual(next(last_iter), 7)
        self.assertEqual(next(last_iter), 8)

    def test_last_less_than_count(self):
        last_iter = Last([1, 2, 3], 10)
        self.assertEqual(next(last_iter), 1)
        self.assertEqual(next(last_iter), 2)
        self.assertEqual(next(last_iter), 3)


if __name__ == '__main__':
    unittest.main()

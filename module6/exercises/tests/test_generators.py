import unittest
from module6.exercises import generators
from module6.exercises.generators import fibonacci


class TestFibonacciGenerator(unittest.TestCase):
    def test_first_fibonacci_numbers(self):
        expected = [0, 1, 1, 2, 3, 5]
        it = fibonacci()
        for i in range(len(expected)):
            self.assertEqual(next(it), expected[i])

    def test_large_sequence(self):
        it = fibonacci()
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i in range(len(expected)):
            self.assertEqual(next(it), expected[i])


if __name__ == '__main__':
    unittest.main()

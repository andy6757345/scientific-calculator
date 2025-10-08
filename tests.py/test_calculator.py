import unittest
import math

class TestCalculator(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(math.sqrt(4), 2)
    def test_fact(self):
        self.assertEqual(math.factorial(5), 120)
    def test_ln(self):
        self.assertEqual(math.log(math.e), 1)
    def test_pow(self):
        self.assertEqual(math.pow(2, 3), 8)

if __name__ == '__main__':
    unittest.main()

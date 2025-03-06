import unittest
from task1 import diagonal_traversing
class TestDiagonalTraversing(unittest.TestCase):
    def test_for_5_5(self):
        self.assertEqual(diagonal_traversing(5, 5), [1, 2, 6, 7, 15, 3, 5, 8, 14, 16, 4, 9, 13, 17, 22, 10, 12, 18, 21, 23, 11, 19, 20, 24, 25])
    def test_for_4_2(self):
        self.assertEqual(diagonal_traversing(4, 2), [1, 2, 3, 5, 4, 6, 7, 8])
    def test_for_1_6(self):
        self.assertEqual(diagonal_traversing(1, 6), [1, 2, 3, 4, 5, 6])
    def test_for_1_1(self):
        self.assertEqual(diagonal_traversing(1, 1), [1]) 
   

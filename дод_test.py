import unittest
from дод import diagonal_traversing_2
class TestDiagonalTraversing(unittest.TestCase):
    def test_for_5_5(self):
        self.assertEqual(diagonal_traversing_2(5, 5),[15, 7, 6, 2, 1, 16, 14, 8, 5, 3, 22, 17, 13, 9, 4, 23, 21, 18, 12, 10, 25, 24, 20, 19, 11])
    def test_for_4_2(self):
        self.assertEqual(diagonal_traversing_2(4, 2), [2, 1, 5, 3, 6, 4, 8, 7])
    def test_for_1_6(self):
        self.assertEqual(diagonal_traversing_2(1, 6), [6, 5, 4, 3, 2, 1])
    def test_for_1_1(self):
        self.assertEqual(diagonal_traversing_2(1, 1), [1]) 
   
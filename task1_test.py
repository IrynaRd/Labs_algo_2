import unittest
from task1 import max_hamsters_number
class TestMaxHamstersNumber(unittest.TestCase):
    def test_for_7_3(self):
        self.assertEqual(max_hamsters_number([[1, 2], [2, 2], [3, 1]], 7), 2)
    def test_for_19_4(self):
        self.assertEqual(max_hamsters_number([[5, 0], [2, 2], [1, 4], [5, 1]], 19), 3)
    def test_for_2_2(self):
        self.assertEqual(max_hamsters_number([[1, 50000], [1, 60000]], 2), 1)


    
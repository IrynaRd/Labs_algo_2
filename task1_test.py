import unittest
from task_1 import prim_algorithm, read_from_file
E, N = read_from_file("islands.csv")
U = {0}
T = []

class TestIndexesDFA(unittest.TestCase):
    def test_ab(self):
        self.assertEqual(prim_algorithm(E, N), [(2.0, 0, 1), (3.0, 1, 2), (5.0, 1, 4), (6.0, 0, 3)])

unittest.main()
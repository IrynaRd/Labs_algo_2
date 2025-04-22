import unittest
from math import inf
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from task1 import dijkstra, find_min_max

class TestGameServerManual(unittest.TestCase):
    def test_for_3_2(self):
        graph = {
            1: [(2, 50)],
            2: [(1, 50), (3, 1000000000)],
            3: [(2, 1000000000)],
        }
        clients = [1, 3]

        self.assertEqual(find_min_max(graph, clients), 1000000000)

    def test_for_9_12(self):
        graph = {
            1: [(2, 20), (4, 20)],
            2: [(1, 20), (3, 20), (5, 10)],
            3: [(2, 20), (6, 20)],
            4: [(1, 20), (7, 20), (5, 10)],
            5: [(2, 10), (4, 10), (6, 10), (8, 10)],
            6: [(3, 20), (5, 10), (9, 20)],
            7: [(8, 20), (4, 20)],
            8: [(7, 20), (9, 20), (5, 10)],
            9: [(6, 20), (8, 20)]
        }
        clients = [2, 4, 6]

        self.assertEqual(find_min_max(graph, clients), 10)

    def test_for_6_6(self):
        graph = {
            1: [(3, 10)],
            2: [(3, 40), (4, 100)],
            3: [(1, 10), (2, 40), (4, 80)],
            4: [(3, 80), (5, 50), (2, 100)],
            5: [(4, 50), (6, 20)],
            6: [(5, 20)]
        }
        clients = [1, 2, 6]

        self.assertEqual(find_min_max(graph, clients), 100)

unittest.main()

from task_1 import indexes_dfa
import unittest

class TestIndexesDFA(unittest.TestCase):
    def test_ab(self):
        self.assertEqual(indexes_dfa("ababacab", "ab"), [0, 2, 6])

    def test_aba(self):
        self.assertEqual(indexes_dfa("ababacab", "aba"), [0, 2])
    
    def test_cab(self):
        self.assertEqual(indexes_dfa("ababacab", "cab"), [5])

unittest.main()
import unittest
from task_1 import count_paths, read_from_file

w, h, matrix = read_from_file("ijones.in")

class TestPathesNumber(unittest.TestCase):
    def test_3_3(self):
        self.assertEqual(count_paths(w, h), 201684)

unittest.main()
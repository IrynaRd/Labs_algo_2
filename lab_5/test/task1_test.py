import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.task1 import min_distance, output_result_in_file

class TestMinDistance(unittest.TestCase):
    def test_output(self):
        test_matrix = [
                [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ]
        expected_res = min_distance(test_matrix)
        expected_output = "Min distance is 11\n"
        output_result_in_file("test_file.txt", expected_res)

        with open("test_file.txt", "r") as f:
            content = f.read()

        self.assertEqual(content, expected_output)



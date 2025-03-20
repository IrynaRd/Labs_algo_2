import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from task1 import BinaryTree, find_successor

class TestFindSuccesor(unittest.TestCase):
    def setUp(self):
        self.root = BinaryTree(10)
        self.root.left = BinaryTree(5, parent=self.root)
        self.root.right = BinaryTree(15, parent=self.root)
        self.root.left.left = BinaryTree(3, parent=self.root.left)
        self.root.left.right = BinaryTree(7, parent=self.root.left)
        self.root.right.right = BinaryTree(20, parent=self.root.right)
        self.root.right.right.left = BinaryTree(12, parent=self.root.right.right)
    
    def test_for_7_3(self):
        node = self.root.left.right
        successor = find_successor(node)
        self.assertEqual(successor.value, 10)
import unittest
from binary_tree import BinaryTreeNode, BinaryTree, PreOrderIterator, PostOrderIterator, InOrderIterator


class TestBinaryTreeIterators(unittest.TestCase):
    def createTree(self):
        n1 = BinaryTreeNode("A")
        n2 = BinaryTreeNode("B")
        n3 = BinaryTreeNode("C", n1, n2)
        n4 = BinaryTreeNode("D")
        n5 = BinaryTreeNode("E", n4, n3)
        n6 = BinaryTreeNode("F", n5)
        n7 = BinaryTreeNode("G")
        n8 = BinaryTreeNode("H", n6, n7)
        self.tree = BinaryTree(n8)

    def test_preorder_iterator(self):
        in_order_values = [node_value for node_value in InOrderIterator(self.tree.root)]
        expected_values = ['D', 'E', 'A', 'C', 'B', 'F', 'H', 'G']
        self.assertEqual(in_order_values, expected_values)

    def test_pre_order_iterator(self):
        # Test PreOrderIterator
        pre_order_values = [node_value for node_value in PreOrderIterator(self.tree.root)]
        expected_values = ['H', 'F', 'E', 'D', 'C', 'A', 'B', 'G']
        self.assertEqual(pre_order_values, expected_values)

    def test_post_order_iterator(self):
        # Test PostOrderIterator
        post_order_values = [node_value for node_value in PostOrderIterator(self.tree.root)]
        expected_values = ['D', 'A', 'B', 'C', 'E', 'F', 'G', 'H']
        self.assertEqual(post_order_values, expected_values)


if __name__ == '__main__':
    unittest.main()

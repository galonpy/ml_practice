"""
CS3C, Assignment #7, Binary Tree
Gabriel Alon
Demo File
Find Maximum Element Recursively
"""

"""
Time/Space Complexity finding max

"""
from gabrielalonLab7 import *
import random
import unittest

class BstTestCase(unittest.TestCase):

    def testAssignmentTree(self):
        """
        printing out the same tree using preorder, and postorder traversals.
        Print out the maximum element found in the binary tree. Give the size and height of the tree.
        """
        bst = BinarySearchTree()
        data = [10,7,6,1,8,9,11,20,14,22]
        for d in data:
            bst.insert(d)
        preorder = BinarySearchTree.formatOutput((bst.preorder())) #expected [10,7,6,1,8,11,20,14,22]
        inorder = BinarySearchTree.formatOutput((bst.inorder())) #expeted [1,6,7,8,9,10,11,14,20,22]
        postorder = BinarySearchTree.formatOutput((bst.postorder())) #expeted  [1,6,9,8,7,14,22,20,11,10]
        print(preorder, "here is preorder")
        print(inorder, "here is inorder")
        print(postorder, "here is postorder")
        print(bst.find_max(), "max") #expected 22
        print(bst.size, "size") #expected 10
        print(bst.height(), "height") #expected 3

        self.assertEqual(hatcher.books[('Darrell Huff', 'How to Lie with Statistics')]['available'], 2, "Testing that the book 'How to Lie with Statistics' has two copies available")


if __name__ == '__main__':
    unittest.main()

"""
The time and Space Complexity for finding the maximum element in the tree
is O(n) because we only have to search through the height of the tree which is at worst linearly increasing with input size

10 7 6 1 8 9 11 20 14 22  here is preorder
1 6 7 8 9 10 11 14 20 22  here is inorder
1 6 9 8 7 14 22 20 11 10  here is postorder
22 max
10 size
3 height
"""
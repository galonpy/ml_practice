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
        print(bst.preorder(), "preorder") #expected [10,7,6,1,8,11,20,14,22]
        print(bst.inorder(), "inorder") #expeted [1,6,7,8,9,10,11,14,20,22]
        print(bst.postorder(), "postorder") #expeted  [1,6,9,8,7,14,22,20,11,10]
        print(bst.find_max(), "max") #expected 22
        print(bst.size, "size") #expected 10
        print(bst.height(), "height") #expected 3
     #   print(bst.formatOutput("ok"))

    def testInit(self):
        bst = BinarySearchTree()
        self.assertIsNone(bst._root)
        self.assertEqual(0, bst.size)
        self.assertEqual(0, len(bst))
     #   print(5)

    def testInsert(self):
        bst = BinarySearchTree()
        bst.insert(23)
        self.assertEqual(23, bst._root.data)
        self.assertIsNone(bst._root.left_child)
        self.assertIsNone(bst._root.right_child)
        self.assertEqual(1, bst.size)

        bst.insert(8)
        self.assertEqual(23, bst._root.data)
        self.assertEqual(8, bst._root.left_child.data)
        self.assertIsNone(bst._root.right_child)
        self.assertEqual(2, bst.size)

        bst.insert(42)
        self.assertEqual(23, bst._root.data)
        self.assertEqual(8, bst._root.left_child.data)
        self.assertEqual(42, bst._root.right_child.data)
        self.assertEqual(3, bst.size)

        bst.insert(4)
        self.assertEqual(23, bst._root.data)
        self.assertEqual(8, bst._root.left_child.data)
        self.assertEqual(42, bst._root.right_child.data)
        self.assertEqual(4, bst._root.left_child.left_child.data)
        self.assertEqual(4, bst.size)

    def testIter(self):
        bst = BinarySearchTree()
        data = [23, 8, 42, 4]
        for d in data:
            bst.insert(d)
        actual = [d for d in bst]
        self.assertEqual(sorted(data), actual)

    def testSum(self):
        bst = BinarySearchTree()
        data = [23, 8, 42, 4]
        for d in data:
            bst.insert(d)
        self.assertEqual(sum(data), sum(bst))

    # find contaains
    def testFindFailure(self):
        bst = BinarySearchTree()
        with self.assertRaises(BinarySearchTree.NotFoundError):
            bst.find("nothing in empty tree")
        data = [23, 8, 42, 4]
        for d in data:
            bst.insert(d)
        with self.assertRaises(BinarySearchTree.NotFoundError):
            bst.find(777)

    def testFindMinEmptyBst(self):
        bst = BinarySearchTree()
        with self.assertRaises(BinarySearchTree.EmptyTreeError):
            bst.find_min()

    def testFindMin(self):
        bst = BinarySearchTree()
        data = [23, 8, 42, 4]
        expected = []
        for d in data:
            expected.append(d)
            bst.insert(d)
            self.assertEqual(min(expected), bst.find_min())

    def testFindMaxEmptyBst(self):
        bst = BinarySearchTree()
        with self.assertRaises(BinarySearchTree.EmptyTreeError):
            bst.find_max()

    def testFindMax(self):
        bst = BinarySearchTree()
        data = [23, 8, 42, 4]
        expected = []
        for d in data:
            expected.append(d)
            bst.insert(d)
            self.assertEqual(max(expected), bst.find_max())

    def testRemove1(self):
        bst = BinarySearchTree()
        data = [23, 8, 42, 4, 31, 79, 56, 91]
        for d in data:
            bst.insert(d)
      #  print(bst)
        data.remove(23)
        bst.remove(23)
       # print(bst)
        actual = [d for d in bst]
        self.assertEqual(sorted(data), actual)
        self.assertEqual(len(data), len(bst))

    def testRemove(self):
        bst = BinarySearchTree()
        random.seed(123)
        data = random.sample(range(1000), 100)
        for d in data:
            bst.insert(d)
        data_to_remove = random.sample(data, len(data))
        for d in data_to_remove:
        #    print(f"removing {d}")
            data.remove(d)
            bst.remove(d)
          #  print(bst)
            actual = [d for d in bst]
            self.assertEqual(sorted(data), actual)
            with self.assertRaises(BinarySearchTree.NotFoundError):
                bst.remove(d)



if __name__ == '__main__':
    unittest.main()

"""
10 7 6 1      8  9      11  20 14    22       preorder
 1   6   7  8  9     10  11  14   20  22      inorder
  1   6     9  8  7     14    22  20  11  10  postorder
22 max
10 size
3 height

"""
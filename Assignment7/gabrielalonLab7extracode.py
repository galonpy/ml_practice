"""
CS3C, Assignment #7, Binary Tree
Gabriel Alon
Main File
"""


class BinarySearchTree:
    class DuplicateDataError(Exception):
        pass

    class EmptyTreeError(Exception):
        pass

    class NotFoundError(Exception):
        pass

    def __init__(self):
        self._root = None
        self._size = 0

    def __iter__(self):
        return self._iter(self._root)

    def _iter(self, subtree_root):
        if subtree_root is None:
            return
        yield from self._iter(subtree_root.left_child)
        yield subtree_root.data
        yield from self._iter(subtree_root.right_child)

    def __str__(self):
        return f"size={self.size}\n" + self._str(self._root, 0)

    def _str(self, subtree_root, depth):
        if subtree_root is None:
            return ""
        s = ""
        s += self._str(subtree_root.left_child, depth + 1)
        s += " " * 4 * depth + str(subtree_root.data) + "\n"
        s += self._str(subtree_root.right_child, depth + 1)
        return s

    def preorder(self):
        return (self._preorder(self._root))

    def _preorder(self, subtree_root):
        if subtree_root is None:
            return ""
        s = ""
        s += str(subtree_root.data) + " "
        s += self._preorder(subtree_root.left_child) + " "
        s += self._preorder(subtree_root.right_child) + " "
        return s

    def postorder(self):
        return (self._postorder(self._root))

    def _postorder(self, subtree_root):
        if subtree_root is None:
            return ""
        s = ""
        s += self._postorder(subtree_root.left_child) + " "
        s += self._postorder(subtree_root.right_child) + " "
        s += str(subtree_root.data) + " "
        return s

    def inorder(self):
        return (self._inorder(self._root))

    def _inorder(self, subtree_root):
        if subtree_root is None:
            return ""
        s = ""
        s += self._inorder(subtree_root.left_child) + " "
        s += str(subtree_root.data) + " "
        s += self._inorder(subtree_root.right_child) + " "
        return s

    def height(self):
        self.height = 0
        return (self._height(self._root, 0))

    def _height(self, subtree_root, height):
        if subtree_root is None:
            return 0
        self._height(subtree_root.left_child, height + 1)
        self._height(subtree_root.right_child, height + 1)
        self.height = max(self.height, height)
        return self.height

    def formatOutput(input):
        result = ""
        for char in (input):
            try:
                if char == " " and result[-1] == " ":
                    continue
                elif char == " ":
                    result+=(" ")
                else:
                    result+=(char)
            except:
                pass
        return result


    @property
    def size(self):
        return self._size

    def __len__(self):
        return self.size

    def insert(self, data):
        self._root = self._insert(self._root, data)

    def _insert(self, subtree_root, data):
        # protects the root from client code
        if subtree_root is None:
            self._size += 1
            return BinaryTreeNode(data)
        if subtree_root.data == data:
            raise BinarySearchTree.DuplicateDataError(f"data {data} already exists")
        elif data < subtree_root.data:
            subtree_root.left_child = self._insert(subtree_root.left_child, data)
        else:
            subtree_root.right_child = self._insert(subtree_root.right_child, data)
        return subtree_root

    ###find contains
    def find(self, data):
        return self._find_node(data).data

    def _find_node(self, data):
        return self._find_node_recursive(self._root, data)

    def _find_node_recursive(self, subtree_root, data):
        if subtree_root is None:
            raise BinarySearchTree.NotFoundError
        if subtree_root.data == data:
            return subtree_root
        elif data < subtree_root.data:
            return self._find_node_recursive(subtree_root.left_child, data)
        else:
            return self._find_node_recursive(subtree_root.right_child, data)

    def __contains__(self, item):
        try:
            self.find(item)
            return True
        except BinarySearchTree.NotFoundError:
            return False

    def find_min(self):
        return self._find_min(self._root)

    def _find_min(self, subtree_root):
        if subtree_root is None:
            raise BinarySearchTree.EmptyTreeError
        #    return self._find_min(subtree_root.left_child)
        try:
            return self._find_min(subtree_root.left_child)
        except BinarySearchTree.EmptyTreeError:
            return subtree_root.data

    def find_max(self):
        return self._find_max(self._root)

    def _find_max(self, subtree_root):
        if subtree_root is None:
            raise BinarySearchTree.EmptyTreeError
        #    return self._find_min(subtree_root.left_child)
        try:
            return self._find_max(subtree_root.right_child)
        except BinarySearchTree.EmptyTreeError:
            return subtree_root.data

    def remove(self, data):
        self._root = self._remove(self._root, data)

    def _remove(self, subtree_root, data):
        if not subtree_root:
            raise BinarySearchTree.NotFoundError(f"data={data} not found")
        if data < subtree_root.data:
            subtree_root.left_child = self._remove(subtree_root.left_child, data)
        elif subtree_root.data < data:
            subtree_root.right_child = self._remove(subtree_root.right_child, data)
        elif subtree_root.left_child and subtree_root.right_child:
            subtree_root.data = self._find_min(subtree_root.right_child)
            subtree_root.right_child = self._remove(subtree_root.right_child, subtree_root.data)
        else:
            subtree_root = subtree_root.left_child if subtree_root.left_child else subtree_root.right_child
            self._size -= 1
        return subtree_root


class BinaryTreeNode:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data  # obect reference to data not a copy of it
        self.left_child = left_child  # reference to root node of left subtree
        self.right_child = right_child

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def left_child(self):
        return self._left_child

    @left_child.setter
    def left_child(self, left_child):
        self._left_child = left_child

    @property
    def right_child(self):
        return self._right_child

    @right_child.setter
    def right_child(self, right_child):
        self._right_child = right_child

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f"data={self._data}, left_child={id(self._left_child)}" \
               f" right_child={id(self._right_child)}"

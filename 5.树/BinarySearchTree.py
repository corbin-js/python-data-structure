class Node:
    __slots__ = '_item' , '_left' , '_right'

    def __init__ (self, item, left=None, right=None):
        self._item = item
        self._left = left
        self._right = right

class BinarySearchTree:

    def __init__ (self, root=None):
        self._root = root
        
    def get(self):
        pass
        
    def add(self):
        pass
        
    def delt(self):
        pass

    def print_preorder(self):
         """
        先序遍历
        """
        pass

    def print_postorder(self):
        """
        后序遍历
        """
        pass

    def print_inorder(self):
        """
        中序遍历
        """
        pass

    def print_breadthfirst(self):
        """
        广度优先遍历
        """
        pass
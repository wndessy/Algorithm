from _ast import List
import unittest

class Node():
    def __init__(self, data):
        self.left_child = None
        self.right_child = None
        self.data = data

class Tree():
    def __int__(self):
        self.root = None

class CreateTrees():
    def __init__(self):
        pass

    def create_binary_tree(self):

        #nodes
        node1 = Node(10)
        node2 = Node(20)
        node3 = Node(30)
        node4 = Node(40)
        node5 = Node(50)
        node6 = Node(60)
        node7 = Node(70)
        node8 = Node(80)

         # add children
        node1.left_child = node2
        node1.right_child = node3

        node2.left_child = node4
        node2.right_child = node5

        node3.left_child = node6
        node3.right_child = node7

        node4.left_child = node8

        my_tree = Tree()
        my_tree.root = node1

        return my_tree

    def create_tree_from_list(self, mylist):
        my_tree = CreateTrees()
        next_id_pointer = 1
        current_node_id = 0
        while next_id_pointer < len(mylist)-1:
            current_node = Node(mylist[current_node_id])
            current_node.left_child = Node(mylist[next_id_pointer])
            next_id_pointer += 1
            current_node.right_child = Node(mylist[next_id_pointer])
            next_id_pointer += 1
            if current_node_id == 0:
                my_tree.root = current_node
            current_node_id += 1
        return my_tree

    def treeTraversal_preorder(self, root, traverse):
        current_node = root
        if current_node:
            print(current_node.data)
            traverse.append(current_node.data)
            self.treeTraversal_preorder(current_node.left_child, traverse)
            self.treeTraversal_preorder(current_node.right_child, traverse)
        return traverse

    def treeTraversal_inorder(self, root, traverse):
        current_node = root
        if current_node:
            self.treeTraversal_preorder(current_node.left_child, traverse)
            print(current_node.data)
            traverse.append(current_node.data)
            self.treeTraversal_preorder(current_node.right_child, traverse)
        return traverse


def treeTraversal_postorder(self, root, traverse):
    current_node = root
    if current_node:
        self.treeTraversal_preorder(current_node.left_child, traverse)
        self.treeTraversal_preorder(current_node.right_child, traverse)
        print(current_node.data)
        traverse.append(current_node.data)
    return traverse


class TestTrees(unittest.TestCase):

    def test_preorder(self):
        tree = CreateTrees()
        mytree = tree.create_binary_tree()
        preorder = tree.treeTraversal_preorder(mytree.root, [])
        self.assertEqual([10,20,40,80,50,30,60,70],preorder)



if __name__ == '__main__':
        # unittest.main()
        tree = CreateTrees()
        # mytree = tree.create_binary_tree()
        # preorder = tree.treeTraversal_preorder(mytree.root)

        mylist = [1,2,3,4,5,6,7,8,9,0]
        mytree = tree.create_tree_from_list(mylist)
        mytree = tree.treeTraversal_preorder(mytree.root, [])





















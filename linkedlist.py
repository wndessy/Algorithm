import unittest


class Node():

    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList():

    def __init__(self, value):
        self.head = Node(value)

    def print_linked_list(self):
        current = self.head.value

        while current.next:
            print(current.next.value)
            current = current.next


class MyLinkedList():
    def create(self):
        my_head = Node(10)
        my_first = Node(20)
        my_second = Node(30)
        my_third = Node(40)
        my_fourth = Node(50)

        # my next pointers
        my_head.next = my_first
        my_first.next = my_second
        my_second.next = my_third
        my_third.next = my_fourth

        # previous pointers

        my_first.previous = my_head
        my_second.previous = my_first
        my_third.previous = my_third
        my_fourth.previous = my_third

        # make a  circle //be carefull print goe infinitely
        # my_fourth.next=my_head
        # my_head.previous=my_fourth

        my_linked_list = LinkedList(my_head)
        my_linked_list.print_linked_list()


class TestMyLinkedList(unittest.TestCase):

    def test_myLinkedList(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    # MyLinkedList().create()
    unittest.main()

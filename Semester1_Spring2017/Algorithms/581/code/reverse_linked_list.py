class LinkedList:

    def __init__(self):
        self.head = None
        return

    def add(self):
        i = 0

        if self.head is None:
            self.head = Node(i)
            return

        current_node = self.head
        prev_node = None

        while not current_node is None:
            i += 1
            prev_node = current_node
            current_node = current_node.next

        prev_node.next = Node(i)

    def traverse(self):
        print "Traverse"
        current_node = self.head

        while not current_node is None:
            print current_node.info
            current_node = current_node.next

    def reverse(self):
        print "Reverse"
        if self.head is None:
            return
        prev_node = None
        current_node = self.head

        while not current_node is None:
            print current_node.info
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        self.head = prev_node

        return


class Node:

    def __init__(self, i):
        self.info = i
        self.next = None


linked_list = LinkedList()

linked_list.add()  # 0
linked_list.add()
linked_list.add()
linked_list.add()
linked_list.add()
linked_list.add()
linked_list.add()
linked_list.add()  # 7

linked_list.traverse()

linked_list.reverse()

linked_list.traverse()

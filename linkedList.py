# Implement a basic singly linked list class in Python. Include methods for appending nodes, inserting nodes at specific positions, and printing the linked list.
class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next

if __name__ == "__main__":
    linked_list = LinkedList()


    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.insert(4)


    print("Initial Linked List:")
    linked_list.print_list()
        
        
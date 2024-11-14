""" This module contains all the basic operations for linked list data structure. """

class LlNode():

    def __init__(self, data):
        self.data = data
        self.next = None

def print_ll(head):
        curr = head
        while curr:
            print(curr.data, end="->")
            curr = curr.next
        print("None")

def delete_node(head, d_node):
     if d_node == head:
          head = head.next
     else:
        curr = head
        while curr:
            if d_node == curr.next:
                 tmp = curr.next
                 curr.next = tmp.next
                 break
            curr = curr.next
     return head

               
if __name__ == "__main__":
    n1 = LlNode(2)
    n2 = LlNode(4)
    n3 = LlNode(6)
    n4 = LlNode(8)
    n5 = LlNode(10)
    n6 = LlNode(12)
    n7 = LlNode(14)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    print_ll(n1)
    n1 = delete_node(n1, n1)
    print_ll(n1)
  

    
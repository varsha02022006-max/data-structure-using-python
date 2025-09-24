class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def is_empty(self):
        return self.head is None
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node
    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def delete(self,data):
        if self.head is None:
            return
        if self.head.data==data:
            self.head=self.head.next
            return
        current=self.head
        while current.next:
            if current.next.data==data:
                current.next=current.next.next
                return
            current=current.next
    def search(self,data):
        current=self.head
        while current:
            if current.data==data:
                return True
            current=current.next
        return False
    def display(self):
        current=self.head
        while current:
            print(current.data,end='->')
            current=current.next
            print("None")
linked_list=Linkedlist()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
print("linked list")
linked_list.display()
linked_list.prepend(0)
linked_list.prepend(-1)
print("linked list after prepend:")
linked_list.display()
linked_list.delete(0)
linked_list.delete(3)
print("linked list after deletions:")
linked_list.display()
print("search for 1:",linked_list.search(1))
print("search for 5:",linked_list.search(5))


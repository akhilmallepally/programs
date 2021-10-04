class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def display(self):
        if self.head == None:
            print("List Empty")
            return
        
        current = self.head
        while current:
            print(current.data)
            current = current.next
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head != None:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_postion(self, pos, data):
        new_node = Node(data)
        if pos < 0:
            print("Invalid position")
            return
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
        counter = 1
        current = self.head
        while current != None:
            if counter == pos:
                new_node.next = current.next
                current.next = new_node
                break
            counter+=1
            current = current.next
            
    def delete_node(self, ele):
        if self.head == None:
            print("List empty")
            return
        if self.head.data  == ele:
            temp = self.head
            self.head = temp.next
            temp = None
            return
        current = self.head
        while current.next != None:
            if current.next.data == ele:
                temp = current.next
                current.next = temp.next
                temp = None
                return
            current= current.next
        print("Element is not found in our list")
        
    def search(self, ele):
        if self.head == None:
            print("List is empty")
            return
        current = self.head
        while current != None:
            if current.data == ele:
                print("Element found")
                return
            current = current.next
            
        
llist = LinkedList()
llist.insert_at_end(40)
llist.insert_at_begin(10)
llist.insert_at_begin(5)
llist.display()
llist.delete_node(40)
llist.display()

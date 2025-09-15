# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    def __init__(self, name):
        self.name = name
        self.next = None

    def __str__(self):
        return self.name
    



# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    def __init__(self):
        self.head = None
        
    def add_front(self,name):
        new_node = Node(name)
        new_node.next = self.head
        self.head= new_node
        
    def add_end(self,name):
        new_node = Node(name)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def remove(self,name):
        current = self.head
        previous = None
        while current:
            if current.name == name:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next
        return False
        
    def print_list(self):
        current = self.head
        if not current:
            print("Waitlist is empty.")
        else:
            while current:
                print(current.name, end=", ")
                current = current.next
            print("none")

        

def waitlist_generator():
    waitlist = LinkedList()
    

    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            waitlist.add_front(name)

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            waitlist.add_end(name)

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            if waitlist.remove(name):
                print(f"{name} removed from the waitlist.")
            else:
                print(f"{name} not found in the waitlist.")
            
        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            waitlist.print_list()
            
            

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program

waitlist_generator()

'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?
My list works by connecting nodes together. Each node holds the value of a customers name and a link to the next node. The list starts with a node called the "head" and after that all of the nodes are liked together in order. 
- What role does the head play?
The head node acts as the beginning or the start to the entire list. It always points to the first node. Without the head it would not know where to start. When adding to the front, the new node becomes the next head and entry point. If the Head is removed then the node next node becomes the head. The head is very important for the structure and organization of tehe lists.
- When might a real engineer need a custom list like this?
A real engineer might need a list when working on systems or problems that want to keep people or objects in order, but also want to add or remove them quickly. For example, if youre building a waitlist for a game ot an application where usuers are joining and leaving at a high rate, a linked list would work well. The list can get as small and large as it need be.

'''
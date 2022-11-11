from person import Person


fileref = open("smallData.csv", "r")  # r is for read
# fileref = open("mediumData.csv", "r") # r is for read
# fileref = open("largeData.csv", "r") # r is for read

lines = fileref.readlines()

first_name = ''
last_name = ''
street = ''
city = ''
state = ''
postcode = ''
people = []

for line in lines:
    last_name, first_name, street, city, state, postcode = line.strip().split(', ')
    person = Person(last_name, first_name, street, city, state, postcode)
    people.append(person)


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data.last_name < self.data.last_name:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data.last_name > self.data.last_name:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


root = Node(0)
for person in people:
    root.insert(person)
# Use the insert method to add nodes

root.insert(Person('Harley', 'Calvert', '10 Margate Avenue', 'FRANKSTON', 'VIC', '3199'))
root.insert(Person('Bob', 'Tranks', '18 Smith St', 'FRANKSTON', 'VIC', '3199'))
root.PrintTree()

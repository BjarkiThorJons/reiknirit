class Node:
    def __init__(self,v):
        self.value = v
        self.left = None
        self.right = None

    def insert(self,d):
        if self.value == d:              # Eru þessi gögn þegar fyrir
            return False
        elif self.value > d:             # Förum vinstra megin
            if self.left:                   # Er til leftChild
                return self.left.insert(d)
            else:
                self.left = Node(d)
                return True
        else:                               # Förum hægra megin
            if self.right:                  # Er til rightChild
                return self.right.insert(d)
            else:
                self.right = Node(d)
                return True
    def preOrderPrint(self):
        print(self.value)
        if self.left:
            self.left.preOrderPrint()
        if self.right:
            self.right.preOrderPrint()
        return True
    def postOrderPrint(self):
        if self.left:
            self.left.postOrderPrint()
        if self.right:
            self.right.postOrderPrint()
        print(self.value)
        return True
    def delete(self,d):
        if self.value == d:
            pass
        else:
            if self.left:
                self.left.delete(d)
            if self.right:
                self.right.delete(d)

class Tree:
    def __init__(self):
        self.root = None

    def insert(self,d):
        if self.root:                       # Er til rót?
            return self.root.insert(d)
        else:
            self.root = Node(d)
            return True

    def preOrderPrint(self):
        if self.root:
           return self.root.preOrderPrint()
    def postOrderPrint(self):
        if self.root:
           return self.root.postOrderPrint()

    def delete(self,n):
        if self.root:
           return self.root.delete()
    def deleteTree(self):
        print("ad")

t = Tree()
t.insert(1)
t.insert(4)
t.insert(5)
t.insert(6)
t.insert(7)
t.insert(20)
t.preOrderPrint()
t.postOrderPrint()

# Bjarki Þór Jónsson
from random import *

print('''
Dæmi 1:
a) Þetta fall raðar talnalista
b) Og þap er kallað Counting sort
c) O(n + k) er flækjustig fallsins ok k er bilið á milli minsta og stærsta staksins

''')

print("Dæmi 2")
# 2
listi = [1, 2, 3, 4, 6, 7, 9]
def linear_search(l,t):
    for x in range(len(l)):
        if t == l[x]:
            return(x)
    return -1

print(linear_search(listi,9))
print("Dæmi 3:")
# 3
def binary_search(l,t,low,high):
    if low<=high and t<=high:
        mid = (high+low)//2
        if t == l[mid]:
            return mid
        elif t > l[mid]:
            return binary_search(l,t,mid+1,high)
        else:
            return binary_search(l,t,low,mid-1)
    else:
        return -1

print(binary_search(listi,5,0,len(listi)))

print('''
Dæmi 4:
    a. O(n)
    b. O(log(n))
''')
print("Dæmi 5:")
# 5
def rada(l,t):
    if len(l) == 0 or l[-1]<t:
        l.append(t)
        return True
    elif t<l[0]:
        l.insert(0,t)
        return True
    for x in range(len(l)):
        if t >= l[x] and t <=l[x+1]:
            l.insert(x+1,t)
            return True
rada(listi,11)
print(listi)

#4
print("Dæmi 6:")
class Node:
    def __init__(self,v):
        self.value = v
        self.left = None
        self.right = None
    def insert(self,d):
        if self.value == d:
            return False
        elif self.value > d:
            if self.left:
                return self.left.insert(d)
            else:
                self.left = Node(d)
                return True
        else:
            if self.right:
                return self.right.insert(d)
            else:
                self.right = Node(d)
                return True
    def find(self,d):
        if self.value == d:
            return True
        elif self.value > d:
            if self.left:
                return self.left.find(d)
            else:
                return False
        else:
            if self.right:
                return self.right.find(d)
            else:
                return False

class Tree:
    def __init__(self):
        self.root = None
    def insert(self,d):
        if self.root:
            return self.root.insert(d)
        else:
            self.root = Node(d)
            return True
    def find(self,d):
        if self.root:
            return self.root.find(d)
        else:
            return False

t = Tree()
print("find 8",t.find(8))
print("insert 6",t.insert(6))
print("insert 2",t.insert(2))
print("insert 3",t.insert(3))
print("insert 7",t.insert(7))

print("find 8",t.find(8))
print("insert 8",t.insert(8))
print("find 8",t.find(8))

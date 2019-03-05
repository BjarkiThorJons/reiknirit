#Bjarki Þór Jónsson
import math
class Node:
    def __init__(self, d):
        self.data = d
        self.prv = None
        self.nxt = None

    # Endurkvæmt fall sem bætir aftast á listann.
    def append(self,d):
        if self.nxt:
            return self.nxt.append(d)
        else:
            curr = Node(d)
            self.nxt = curr
            curr.prv = self
            return True

    # Endurkvæmt fall sem og prentar listann.
    def printList(self):
        print(self.data)
        if self.nxt:
            return self.nxt.printList()

    # Endurkvæmt fall sem og prentar listann frá Head til enda
    def find(self, d):
        if self.data == d:
            return True
        elif self.nxt:
            return self.nxt.find(d)
        else:
            return False
    # Endurkvæmt fall sem eyðir ákveðnum hnút úr lista
    def delete(self, d):
        if self.data == d:
            self.prv.nxt = self.nxt
            if self.nxt:
                self.nxt.prv = self.prv
            self.nxt = None
            self.prv = None
            return True
        elif self.nxt:
            return self.nxt.delete(d)
        else:
            return False
class DLL: # DLL = Dobule Linked List
    def __init__(self):
        self.head = None

    # Bætir við fremst á listann, hnúturinn verður Head -> förum ekki í Node klasann.  Þú úrfærir fallið í þessum klasa
    def push(self,d):
        s = Node(d)
        s.nxt = self.head
        self.head.prv = s
        self.head = s
        return True
    # Bætir við aftast á listann -> kallar á endurkvæmnt fall í Node.  Fallið er þegar útfært í Node klasa
    def append(self, d):
        if self.head:
            return self.head.append(d)
        else:
            self.head = Node(d)
            return True

    # Prentar listann allan á skjá -> kallar á endurkvæmt fall í Node, þú útfærir printList í Node.  Notaðu endurkvæmni.
    def printList(self):
        if self.head:
            self.head.printList()
        else:
            print("Empty list!")

    # Kallar á endurkvæmt fall í Node klasanum, finnur ákveðinn hnút.  Þú útfærir fallið find í Node klasanum.  Notaðu endurkvæmni.
    def find(self, d):
        if self.head:
            return self.head.find(d)
        else:
            return False

    # Kallar á endurkvæmt fall í Node klasanum, finnur ákveðinn hnút og eyðir.  Þú útfærir fallið delete í Node klasanum.  Notaðu endurkvæmni.
    def delete(self, d):
        if self.head is None:
            return -1
        elif self.head.data == d:
            self.head = self.head.nxt
            self.head.prv.nxt = None
            self.head.prv = None
            return True
        else:
            return self.head.delete(d)


class Vigur:

    # Smiður frumstillir x og y hnit vigurs eftir parametrum
    def __init__(self,x,y):
        self.x = x
        self.y = y

    # Fall sem skrifar hnit vigurs á skjá
    def prenta(self):
        print(self.x,",",self.y)

    # Fall sem skilar lengd
    def lengd(self):
        return(round(math.sqrt((self.x**2)+(self.y**2))))
    # Fall sem skilar hallatölu
    def halli(self):
        return(self.y/self.x)
    # Fall sem skilar þvervigri
    def þvervigur(self):
        return Vigur(-self.y,self.x)

    # Fall sem skilar stefnuhorni
    def stefnuhorn(self):
        t = math.degrees(math.atan(self.y/self.x))
        if self.x > 0:
            return t
        elif self.x < 0:
            if self.y > 0:
                return 180+t
            else:
                return t-180

    # Fall sem tekur vigur sem parameter og skilar horni milli vigra
    def horn(self,v):
        a = math.sqrt((self.x**2)+(self.y**2))
        b = math.sqrt((v.x**2)+(v.y**2))
        ab = (self.x * v.x) + (self.y * v.y)
        h = math.acos(ab/(a*b))
        return math.degrees(h)
    # Fall sem tekur vigur sem parameter og skilar summu vigri
    def summa(self,v):
        return Vigur(self.x+v.x,self.y+v.y)
print("----LINKED LISTI----")
dbl = DLL()
dbl.append(5)           # 5
dbl.append(7)           # 5 7
dbl.push(1)             # 1 5 7
dbl.push(0)             # 0 1 5 7
dbl.append(10)          # 0 1 5 7 10
dbl.printList()
print()
print(dbl.delete(10))   # 0 1 5 7
dbl.printList()
print(dbl.find(5))      # True
print(dbl.find(10))     # False

# Keyrsluforrit
print("----VIGUR----")
v1 = Vigur(-3,-3)
v1.prenta()
print("Lengd: ", v1.lengd())
print("Halli: ", v1.halli())
vþ = v1.þvervigur()
print("Þvervigur: " , end=" ")
vþ.prenta()
print("Stefnuhorn: ", v1.stefnuhorn())
v2 = Vigur(-3,1)
print("Horn milli vigra: " , v2.horn(v1))
v3 = v1.summa(v2)
print("Summa: " , end=" ")
v3.prenta()

# Bjarki Þór Jónsson
from random import *
# 2
listi = [1, 2, 3, 4, 5, 6, 7, 8, 9]
listinn = []

def linear_search(l,t):
    for x in range(len(l)):
        if t == l[x]:
            return(x)
    return -1

# print(linear_search(listi,6))
# 3
def binary_search(l,t,low,high):
    if low<high:
        mid = (high+low)//2
        if t == l[mid]:
            return mid
        elif t > l[mid]:
            return binary_search(l,t,mid+1,high)
        else:
            return binary_search(l,t,low,mid-1)
    else:
        return -1

print(binary_search(listi,2,0,len(listi)))
'''
4.
    a. O(n)
    b. O(log(n))
'''

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
rada(listi,8)
print(listi)
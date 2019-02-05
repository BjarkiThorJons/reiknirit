#Bjarki Þór Jónsson
import string
import sys
'''
2.
	2^(n-1)

3.
	a. ein lykkja sem keyrir n sinnum
	b. lykkja inn í lykkju
	c. forrit sem notar divide and conquer  ?? t.d skipti sortuðum listi í tvent og leita í einum þangað til forritið fynnur hvað það er að leita af ??
'''
#4
listi = list(string.ascii_lowercase)
tala = 2
teljari = 0
listinn =[]

def strengur(n,s="",t = 0):
    if n > 0:
        for x in range(t,len(listi)):
            if n == 1:
                print(s+listi[x])
                listinn.append(s+listi[x])
            t+=1
            strengur(n-1,s+listi[x],t)

strengur(3)
# 5
sys.setrecursionlimit(15000)
listinn.reverse()
print(listinn)
tolulisti = ["ad","ab","aa","ag","as","ac"]

if "abc" > "acb":
    print("abc")
def partiton(l,low,high):
    t = low-1
    for x in range(low,high):
        if l[x] <= l[high]:
            t+=1
            l[x], l[t] = l[t], l[x]
    l[t+1], l[high] = l[high], l[t+1]
    return t+1


def quicksort(l,low,high):
    if low<high:
        ind = partiton(l,low,high)
        quicksort(l,low,ind-1)
        quicksort(l,ind+1,high)


quicksort(listinn,0,len(listinn)-1)
print(listinn)

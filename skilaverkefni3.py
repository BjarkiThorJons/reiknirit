#Bjarki Þór Jónsson
import string
import sys
from time import perf_counter
'''
2.
	O(2^(n-1))

3.
	a. ein lykkja sem keyrir n sinnum
	b. lykkja inn í lykkju
	c. forrit sem notar divide and conquer t.d skipti sortuðum listi í tvent og leita í einum þangað til forritið fynnur hvað það er að leita af
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
                listinn.append(s+listi[x])
            t+=1
            strengur(n-1,s+listi[x],t)
ta = int(input("Veldu lengd: "))
start = perf_counter()
strengur(ta)
print(len(listinn))
print(perf_counter()-start)
'''
a.
   26!
_________
(26-n)!*n!
b.
O(2^n)

'''
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
'''
5
	a.
	b. O(n2)

runtime fyrir forrit í lið 4
1:
fjöldi strengja: 26
timi: 2.251300000000178e-05
2:
fjöldi strengja: 325
timi: 0.00022446700000000597
3:
fjöldi strengja: 2600
timi: 0.0018314909999999907
4:
fjöldi strengja: 14950
timi: 0.011072375999999995
5:
fjöldi strengja: 65780
timi: 0.053350946999999996
6:
fjöldi strengja: 230230
timi: 0.20211786899999998
7:
fjöldi strengja: 657800
timi: 0.651940911
8:
fjöldi strengja: 1562275
timi: 1.678722658
9:
fjöldi strengja: 3124550
timi: 3.8532628819999997
10:
fjöldi strengja: 5311735
timi: 7.742063373999999
11:
fjöldi strengja: 7726160
timi: 13.277992975
12:
fjöldi strengja: 9657700
timi: 20.013862651
13:
fjöldi strengja: 10400600
timi: 27.644872851000002
14:
fjöldi strengja: 9657700
timi: 35.057557548000005
15:
fjöldi strengja: 7726160
timi: 40.89774241899998
16:
fjöldi strengja: 5311735
timi: 44.895888746
17:
fjöldi strengja: 3124550
timi: 47.79471476399999
18:
fjöldi strengja: 1562275
timi: 49.04750884800001
19:
fjöldi strengja: 657800
timi: 50.74615873600004
20:
fjöldi strengja: 230230
timi: 49.82848776200001
21:
fjöldi strengja: 65780
timi: 50.19905346499996
22:
fjöldi strengja: 14950
timi: 49.77317455100001
23:
fjöldi strengja: 2600
timi: 49.737399891999985
24:
fjöldi strengja: 325
timi: 49.776428658999976
25:
fjöldi strengja: 26
timi: 50.179238798999904
26:
fjöldi strengja: 1
timi: 50.014282781999995
'''

# Bjarki Þór Jónsson

"""
1.



2.  Forritið býr til fall sem tekur inn tölu.
    Ef talan er stærri en 0 kallar forritið á fallið aftur og lætur töluna deilt með 2 með engum aukastöfum.
    Prentar síðan töluna modulus 2
"""


# 3
def summa(n):
    if n == 1:
        return n
    else:
        return n*n + summa(n-1)


print(summa(5))
print("----4----")


# 4
def runa(n):
    if n == 1:
        print(n)
    else:
        runa(n-1)
        print(n*(n+1)//2)


runa(7)
print("----5----")
def þversumma(n):
    if len(n) == 1:
        return int(n)
    else:
        return int(n[0]) + þversumma(n[1:])

print(þversumma("1209"))
print("----6----")
def samnefnari(n,m):
    if n == m or m == 0:
        return n
    else:
        return samnefnari(m,n%m)

print(samnefnari(6,82))

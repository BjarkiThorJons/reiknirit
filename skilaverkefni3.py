import string
listi = list(string.ascii_lowercase)
def strengur(n,s="",t = 0):
    if n > 0:
        for x in range(t,len(listi)):
            if n == 1:
                print(s+listi[x])
            t+=1
            strengur(n-1,s+listi[x],t)

strengur(4)
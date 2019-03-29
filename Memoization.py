#Bjarki Þór Jónsson
k = {}
f = open("triangle2.txt","r")
listi = f.read().split("\n")
for x in range(len(listi)):
   listi[x] = listi[x].split(" ")
print(listi)
def path(listi,ts,ls):
    key = str(ts)+","+str(ls)
    if key in k:
        return k[key]
    if len(listi)-2 == ls:
        gildi = int(listi[ls][ts]) + max(int(listi[ls+1][ts+1]), int(listi[ls+1][ts]))
        k[key] = gildi
        return gildi
    else:
        s1 = path(listi,ts,ls+1)
        s2 = path(listi,ts+1,ls+1)
        gildi = int(listi[ls][ts]) + max(s1,s2)
        k[key] = gildi
        return gildi
s = path(listi,0,0)
print(s)

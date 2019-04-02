#Bjarki Þór Jónsson
k = {}
f = open("triangle.txt","r")
listi = f.read().split("\n")
l = {}
for x in range(len(listi)):
   listi[x] = listi[x].split(" ")
t = 1
def path(listi,ts,ls,t):
    key = str(ts)+","+str(ls)
    if key in k:
        return k[key]
    if len(listi)-2 == ls:
        gildi = int(listi[ls][ts]) + max(int(listi[ls+1][ts+1]), int(listi[ls+1][ts]))
        k[key] = gildi
        l[t]= str(max(int(listi[ls+1][ts+1]), int(listi[ls+1][ts])))
        return gildi
    else:
        s1 = path(listi,ts,ls+1,t)
        s2 = path(listi,ts+1,ls+1,t)
        gildi = int(listi[ls][ts]) + max(s1,s2)
        tala = max(listi[ls+1][ts+1],listi[ls+1][ts])
        l[t]+=","+str(tala)
        print(l)
        k[key] = gildi
        #print(k)
        return gildi



s = path(listi,0,0,t)
print(s)
listinn = l[1].split(",")

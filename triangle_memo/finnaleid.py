#Bjarki Þór Jónsson
k = {}
f = open("triangle2.txt","r")
listi = f.read().split("\n")
l = {}
for x in range(len(listi)):
   listi[x] = listi[x].split(" ")
t = 1
def path(listi,ts,ls,t):
    key = str(ts)+","+str(ls)
    if key in k:
        return list(k[key].keys())[0]
    if len(listi)-2 == ls:
        gildi = int(listi[ls][ts]) + max(int(listi[ls+1][ts+1]), int(listi[ls+1][ts]))
        k[key] = {gildi:listi[ls][ts]+","+str(max(int(listi[ls+1][ts+1]), int(listi[ls+1][ts])))}
        #print(k)
        return gildi
    else:
        s1 = path(listi,ts,ls+1,t)
        s2 = path(listi,ts+1,ls+1,t)
        gildi = int(listi[ls][ts]) + max(s1,s2)
        if s1 >s2:
            k[key] = {gildi:listi[ls][ts]+","+k[str(ts)+","+str(ls+1)][s1]}
        elif s2 >= s1:
            k[key] = {gildi:listi[ls][ts]+","+k[str(ts+1)+","+str(ls+1)][s2]}
        #print(k)
        return gildi



s = path(listi,0,0,t)
#print(s)
summa = 0
for x in k.values():
    if s == list(x.keys())[0]:
        print(x)
        listi = x[s].split(",")
        for x in listi:
            summa+=int(x)
        print(summa)


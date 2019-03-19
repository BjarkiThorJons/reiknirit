#Bjarki Þór Jónsson
k = {}
f = open("triangle.txt","r")
listi = f.read().split("\n")
for x in range(len(listi)):
   listi[x] = listi[x].split(" ")
print(listi)
def path(listi,ts,ls):
    if len(listi)-2 == ls:
        print(int(listi[ls+1][ts+1]), int(listi[ls+1][ts]))
        return int(listi[ls][ts]) + max(int(listi[ls+1][ts+1]), int(listi[ls+1][ts]))
    else:
        s1 = path(listi,ts,ls+1)
        s2 = path(listi,ts+1,ls+1)
        return int(listi[ls][ts]) + max(s1,s2)
s = path(listi,0,0)
print(s)

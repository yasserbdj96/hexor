import sys
from hexor import hexor

#
try:
    m=tuple(map(int,sys.argv[1].split(',')))
    x=int(sys.argv[2])
except ZeroDivisionError:
    print(f"Usage: python3 {sys.argv[0]} RGB RANGE\n ex: python3 {sys.argv[0]} 255,0,0 50")
    exit()
finally:
    pass
#
p1=hexor(True,"hex")

#
colors=[]
mxd=[0,0,0]
mxu=[255,255,255]

#
for g in range(0,3):
    if not m[g]-x<=0:
        mxd[g]=m[g]-x

#
for f in range(0,3):
    if not m[f]+x>=255:
        mxu[f]=m[f]+x

#
for i in range(mxd[0],mxu[0]+1):
    for j in range(mxd[1],mxu[1]+1):
        for k in range(mxd[2],mxu[2]+1):
            colors.append('#%02x%02x%02x'%(i,j,k))

#
k=""
for i in range(len(colors)):
    bg=colors[i]
    if i%18==0:
        print(k)
        k=""
    else:
        k+=p1.c(f" {bg} ","#ffffff",bg)
print(k)

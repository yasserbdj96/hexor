import sys
from hexor import hexor

#
try:
    m=tuple(map(int,sys.argv[1].split(',')))
    x=int(sys.argv[2])
except:
    print(f"Usage: python3 {sys.argv[0]} RGB RANGE\n ex: python3 {sys.argv[0]} 255,0,0 50")
    exit()
#
p1=hexor(True,"hex")

#
colors=[]
mxd=[0,0,0]
mxu=[255,255,255]

#
if not m[0]-x<=0:mxd[0]=m[0]-x
if not m[1]-x<=0:mxd[1]=m[1]-x
if not m[2]-x<=0:mxd[2]=m[2]-x

#
if not m[0]+x>=255:mxu[0]=m[0]+x
if not m[1]+x>=255:mxu[1]=m[1]+x
if not m[2]+x>=255:mxu[2]=m[2]+x

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

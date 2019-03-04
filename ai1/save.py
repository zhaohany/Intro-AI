import numpy as np
import random
import math


def printmap(map,sx,sy,gx,gy):
    map[sx][sy][0]=6
    map[gx][gy][0]=9
    for x in range(10):
        print("\n")
        for y in range(10):
            print(map[x][y][0]),


def findmin(open):
    if len(open) == 1:
        return 0
    else:
        # print(open)
        min = 10000
        i=0
        # print(i)
        # print(len(open))
        while i < len(open):
            x=open[i][2]
            #print(x)
            if x <= min :
                index=i
                min=x
            i+=1
            # print(i)
            # print(len(open))
        # open.pop(index)
        return index



def heap_push(open,cango):
    open=open+cango
    return open

def heap_pop(open):
    index=findmin(open)
    return index

def move(current,close):
    current[1]=1
    close.append(current)
    return close


def neibor_check(map,p,gx,gy):
    cango = []
    x=p[4]
    y=p[5]
    up_x=x-1
    up_y=y
    down_x=x+1
    down_y=y
    left_x=x
    left_y=y-1
    right_x=x
    right_y=y+1
    g=map[x][y][3]
    if -1< up_x <= 9 and -1< up_y <=9 and map[up_x][up_y][0]!= 1 and map[up_x][up_y][1] != 1:
        map[up_x][up_y][2]=g+manhadun(up_x,up_y,gx,gy)
        map[up_x][up_y][3]=g+1
        cango.append(map[up_x][up_y])
        # print(cango)

    if -1< down_x <= 9 and -1< down_y <=9 and map[down_x][down_y][0]!= 1 and map[down_x][down_y][1] != 1:
        map[down_x][down_y][2]=g+manhadun(down_x,down_y,gx,gy)
        map[down_x][down_y][3]=g+1
        cango.append(map[down_x][down_y])
        # print(cango)
    if -1< left_x <= 9 and -1< left_y <=9 and map[left_x][left_y][0]!= 1 and map[left_x][left_y][1] != 1:
        map[left_x][left_y][2]=g+manhadun(left_x,left_y,gx,gy)
        map[left_x][left_y][3]=g+1
        cango.append(map[left_x][left_y])
        # print(cango)
    if -1< right_x <= 9 and -1< right_y <=9 and map[right_x][right_y][0]!= 1 and map[right_x][right_y][1] != 1:
        map[right_x][right_y][2]=g+manhadun(right_x,right_y,gx,gy)
        map[right_x][right_y][3]=g+1
        cango.append(map[right_x][right_y])
        # print(cango)

    return cango



def manhadun(p1x,p1y,p2x,p2y):#maparray[0][3][3]  he maparray[0][4][4]    manhadun(3,3,4,4)
    dx=abs(p1x-p2x)
    dy=abs(p1y-p2y)
    d=dx+dy
    return d

map = np.zeros((10, 10, 6))
for x in range(0,10):
    for y in range(0,10):
        map[x][y][4]=x
        map[x][y][5]=y
        if random.randint(1,10) <=7:
            map[x][y][0]=0
        else:
            map[x][y][0]=1
starx=random.randint(1,9)
stary=random.randint(1,9)
goalx=random.randint(1,9)
goaly=random.randint(1,9)

while (goalx==starx and goaly == stary) or (map[starx][stary][0]==1 and map[goalx][goaly][0]==1):
    starx=random.randint(1,9)
    stary=random.randint(1,9)
    goalx=random.randint(1,9)
    goaly=random.randint(1,9)

#starx,stary,goalx,goaly
print("Goalpoint:"+repr(goalx)+","+repr(goaly)+";Starpoint:"+repr(starx)+","+repr(stary))
open = []
close = []
cango = []
map[starx][stary][1]=1

open.append(map[starx][stary])
suc=0
print("map is")
printmap(map,starx,stary,goalx,goaly)
print("map over")
while len(open) != 0:
    #print(open)
    index=heap_pop(open)

    current=open.pop(index)
    #print(current)
    # print(current[4])
    # print(current[5])
    if current[4] == goalx and current[5] == goaly:
        print("reached goal")
        suc=1
        break
    else:
        cango=neibor_check(map,current,goalx,goaly)
        open=heap_push(open,cango)
        map[current[4]][current[5]][1]=1
        close.append(current)

if suc == 0:
    print("failed")
else:
    print("success")
    print(close)




#
#
# f=0+manhadun(starx,stary,goalx,goaly)
# map[starx][stary][3]=0
# open.append(map[starx][stary])
# cango=[]
# cango=neibor_check(map,starx,stary)
# open=heap_push(open,cango)

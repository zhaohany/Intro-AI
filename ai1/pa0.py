import numpy as np
import random

#report:  p1:a) fx=gx+hx  fx for east is less tha north
            #b) 
# class node:
#     def __init__(self, block=None, create=None, g=None, visited=None):
#         self.block=block
#         self.create=create
#         self.g=g
#         self.visited=visited
#
# n1=node(1,1,7,1)
# print("Block:"+repr(n1.block)+"create:"+repr(n1.create)+"g:"+repr(n1.g)+"visited:"+repr(n1.visited))
def mapgenerator(): #This function will generate 50 2d array each point in the form [0 0 0 0] represent
    maparray=[]
    for z in range(0,50):
        map = np.zeros((101, 101, 4))
        for x in range(0,101):
            for y in range(0,101):
                if random.randint(1,10) <=7:
                    map[x][y][0]=0
                else:
                    map[x][y][0]=1
        maparray.append(map)

    # print(len(maparray))
    # print(maparray[0])
    print("50 maps successfully generated")
def manhadun(p1x,p1y,p2x,p2y):#maparray[0][3][3]  he maparray[0][4][4]    manhadun(3,3,4,4)
    dx=abs(p1x-p2x)
    dy=abs(p1y-p2y)
    d=dx+dy
    print("Manhadun distance is:"+repr(d))





mapgenerator()
manhadun(3,3,4,4)

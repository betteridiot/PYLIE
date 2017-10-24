#! /usr/bin/env python

import numpy as np

class Grid2D(object):
    def __init__(self,
                 xmin=0, xmax=1, dx=0.5,
                 ymin=0, ymax=1, dy=0.5):
        
        self.xcoor = np.arange(xmin, xmax+dx, step=dx)
        self.ycoor = np.arange(ymin, ymax+dy, step=dy)
    
    @profile
    def gridloop(self, f):
        lx = np.size(self.xcoor)
        ly = np.size(self.ycoor)
        a = np.zeros((lx,ly))

        for i in range(lx):
            x = self.xcoor[i]
            for j in range(ly):
                y = self.ycoor[j]
                a[i,j] = f(x, y)
        return a

def myfunc(x, y):
    return np.sin(x*y) + y

if __name__ == "__main__":
    g = Grid2D(dx=0.001, dy=0.001)
    print("Computing values...")
    a = g.gridloop(myfunc)
    print("done")

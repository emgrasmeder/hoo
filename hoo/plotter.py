# From Tom Elliot's blog (http://telliott99.blogspot.com/)
# The following code creates randomly located points and draws them together with arrows,
# which is pretty neat.
# This will be edited in the coming days to accomodate plotting our cars. 


import numpy as np
import matplotlib.pyplot as plt

def drawArrow(x, y, w, h, i):
    a = plt.Arrow(x,y,w,h,
                  width=0.05,zorder=i+1)
    a.set_facecolor('0.7')
    a.set_edgecolor('w')

def getArrow(p1,p2,i):
    # we need to subtract some from each end
    # slope = m
    w = p2.x - p1.x
    h = p2.y - p1.y
    
    dr = 0.03
    if w == 0:
        dy = dr
        dx = 0
    else:
        theta = np.arctan(np.abs(h/w))
        dx = dr*np.cos(theta)
        dy = dr*np.sin(theta)
    
    if w < 0:
        dx *= -1
    if h < 0:
        dy *= -1
    w -= 2*dx
    h -= 2*dy
    x = p1.x + dx
    y = p1.y + dy
    
    a = draw_arrow(x, y, w, h, i)
    
    return a

class Point:
    pass

N = 10
L = np.random.uniform(size=N*2)
pL = list()
for i in range(0,N*2,2):
    p = Point()
    p.x,p.y = L[i],L[i+1]
    pL.append(p)
    
ax = plt.axes()
for i,p in enumerate(pL):  
    if i:
        a = getArrow(pL[i-1],p,i)
        ax.add_patch(a)
    plt.scatter(p.x,p.y,s=250,zorder=1)

ax.set_xlim(-0.01,1.01)
ax.set_ylim(-0.01,1.01)

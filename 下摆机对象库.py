import math
class 透镜():
    r=0.0
    d=0.0

class 精磨基模():
    r=0.0
    d=0.0
    h=0.0

class 精磨修模():
    r=0.0
    d=0.0
    h=0.0

class 抛光基模():
    r=0.0
    d=0.0
    h=0.0

class 抛光修模():
    r=0.0
    d=0.0
    h=0.0

class 返修抛光基模():
    r=0.0
    d=0.0
    h=0.0

class 抛光修模对修模():
    r=0.0
    d=0.0
    h=0.0

class 粗磨模():
    r=0.0
    d=0.0
    h=0.0

def 计算矢高(r,d):
    h=math.fabs(r)-math.sqrt(r**2-(d/2)**2)
    return h
def rx_and_dx(r,d,a,t):
    r1=math.fabs(r)
    if r>0:
        rx=-(r1+t)
        dx=math.fabs(rx)*math.sin(a)*2
    else:
        rx = r1 - t
        dx = d
    return rx,dx
    
import tkinter as tk
from tkinter import ttk
from 下摆机对象库 import *
import math
win=tk.Tk()
win.title('下摆机模具设计')
w,h=win.maxsize()
win.geometry("{}x{}".format(w,h))
f1=tk.Frame(win)
f1.pack()
l1=tk.Label(f1,text='透镜半径')
l1.grid(row=1,column=0)
e1=tk.Entry(f1, show=None)
e1.grid(row=1,column=1)
l2=tk.Label(f1,text='透镜口径')
l2.grid(row=3,column=0)
e2=tk.Entry(f1, show=None)
e2.grid(row=3,column=1)
var=tk.IntVar()
xuanze=1
var.set(1)
def 选择():
    global xuanze
    xuanze=var.get()
    
xbj_r=tk.Radiobutton(f1,text='下摆机',variable=var,value=1,command=选择)
xbj_r.grid(row=4,column=0)
pbj_r=tk.Radiobutton(f1,text='平摆机',variable=var,value=2,command=选择)
pbj_r.grid(row=5,column=0)

def 计算():
    
    透镜.r=float(e1.get())
    透镜.d=float(e2.get())
    r=math.fabs(透镜.r)
    
    b = (math.pi / 2 - math.acos(透镜.d / (2 * r))) / 2  #倾斜角弧度值
    if xuanze==1:
        k = round(1 + (2 - 透镜.d / r) / 2,3)  #摆动系数
        xs_var.set(k)
        s = round(透镜.d / r,3)   #D/R的值
        b1 = b * 180 / math.pi   #倾斜角度数
        dr_var.set(s)
        qx_var.set(round(b1,2))
        b1 = b1 * k  #摆动角度数
        bd_var.set(round(b1,2))
        b = b*(k + 2)    #球模张角
        if b>(math.pi/2):
            b = math.pi / 2
        dm = r * math.sin(b) * 2    #球模口径
        
        a = math.asin(dm / r / 2)
        #hm=计算矢高(r,dm)    #球模矢高
        kj_var.set(str(round(dm,2)))  #在文本框中显示球模口径
        k = 1.1 + (175 - dm) / 1500    #摆动系数
        if r>20:
            rj,dj=rx_and_dx(透镜.r,dm,a,3)   #精磨基模的半径和口径
            hj=计算矢高(rj,dj)    #矢高
        else:
            rj=0.0
            hj=0.0
            dj=dm
        if rj!=0.0:
            rj=round(rj,3)   #显示3位小数
        if dj!=0.0:
            dj=round(dj,1)
        if hj!=0.0:
            hj=round(hj,2)
        jjbj_var.set(rj)
        jjkj_var.set(dj)
        jjsg_var.set(hj)
        if 透镜.r>0.0:
            rjx=r     #精磨修模半径
            djx=dm*k   #精磨修模口径
            if djx>math.fabs(rjx*2):
                djx=math.fabs(rjx*2)
        if 透镜.r<0.0:
            rjx=-r
            djx=dm
            if djx>math.fabs(rjx*2):
                djx=math.fabs(rjx*2)
        hjx=计算矢高(rjx,djx)    #精磨修模矢高
        if djx!=0.0:
            djx=round(djx,1)
        if hjx!=0.0:
            hjx=round(hjx,2)
        jxbj_var.set(rjx)
        jxkj_var.set(djx)
        jxsg_var.set(hjx)
        rp1,dp1=rx_and_dx(透镜.r,dm,a,0.5)    #抛光基模半径和口径
        hp1=计算矢高(rp1,dp1)       #抛光基模矢高
        pjbj_var.set(round(rp1,3))
        pjkj_var.set(round(dp1,1))
        pjsg_var.set(round(hp1,2))
        rp2,dp2=rx_and_dx(透镜.r,dm,a,0.8)    #返修抛光基模半径和口径
        hp2=计算矢高(rp2,dp2)       #返修抛光基模矢高
        fpjbj_var.set(round(rp2,3))
        fpjkj_var.set(round(dp2,1))
        fpjsg_var.set(round(hp2,2))
        if r>20.0:
            rp3,dp3=rx_and_dx(-透镜.r,dm,a,3)   #抛光修模半径和口径
            if 透镜.r>0.0:
                dp3=dp3*k
                if dp3>math.fabs(rp3*2):
                    dp3=math.fabs(rp3*2)
            hp3=计算矢高(rp3,dp3)    #抛光修模矢高
        else:
            rp3=0.0
            hp3=0.0
            if 透镜.r>0.0:
                dp3 = dm * k
                if dp3>r*2:
                    dp3=r*2
            else:
                dp3=dm
        if rp3!=0.0:
            rp3=round(rp3,3)
        if hp3!=0.0:
            hp3=round(hp3,2)
        pxbj_var.set(rp3)
        pxkj_var.set(dp3)
        pxsg_var.set(hp3)
        if 透镜.r>0.0:
            rp4=-r     #抛光修模对修模半径
            dp4 = dm * k     #抛光修模对修模口径
            
            if dp4>math.fabs(rp4)*2:
                dp4=math.fabs(rp4)*2
        if 透镜.r<0.0:
            rp4=r
            dp4 = dm * k
            
            if dp4>math.fabs(rp4)*2:
                dp4=math.fabs(rp4)*2
        hp4=计算矢高(rp4,dp4)     #抛光修模对修模矢高
        pxdbj_var.set(round(rp4,3))
        pxdkj_var.set(round(dp4,1))
        pxdsg_var.set(round(hp4,2))
    elif xuanze==2:
        k = 1.1 + (175 - 透镜.d) / 1500    #摆动系数
        xs_var.set(round(k,3))
        s=透镜.d/r               #D/R的值
        b1=b*180/math.pi         #倾斜角
        dr_var.set(round(s,3))
        qx_var.set(round(b1,2))
        b1 = b1 * k              #摆动角
        bd_var.set(round(b1,2))
        dm = 透镜.d * k               #球模口径
        if dm>r*2:
            dm=r*2
        a=math.asin(dm/r/2)
        kj_var.set(round(dm,1))
        rj,dj=rx_and_dx(透镜.r,dm,a,3)   #精磨基模半径和口径
        hj=计算矢高(rj,dj)      #精磨基模矢高
        jjbj_var.set(round(rj,3))
        jjkj_var.set(round(dj,1))
        jjsg_var.set(round(hj,2))
        if 透镜.r>0.0:
            rjx = r        #精磨修模半径
            djx = dm * k   #精磨修模口径
            if djx>rjx*2:
                djx=rjx*2
        else:
            rjx=-r
            djx=dm
        hjx=计算矢高(rjx,djx)  #精磨修模矢高
        jxbj_var.set(round(rjx,3))
        jxkj_var.set(round(djx,1))
        jxsg_var.set(round(hjx,2))
        rp1,dp1=rx_and_dx(透镜.r,dm,a,0.5)    #抛光基模半径和口径
        hp1=计算矢高(rp1,dp1)      #抛光基模矢高
        pjbj_var.set(round(rp1,3))
        pjkj_var.set(round(dp1,1))
        pjsg_var.set(round(hp1,2))
        rp2,dp2=rx_and_dx(透镜.r,dm,a,0.8)    #返修抛光基模半径和口径
        hp2=计算矢高(rp2,dp2)      #返修抛光基模矢高
        fpjbj_var.set(round(rp2,3))
        fpjkj_var.set(round(dp2,1))
        fpjsg_var.set(round(hp2,2))
        rp3,dp3=rx_and_dx(-透镜.r,dm,a,3)     #抛光修模半径和口径
        if 透镜.r>0.0:
            dp3=dp3*k
            if dp3>math.fabs(rp3)*2:
                dp3=math.fabs(rp3)*2
        hp3=计算矢高(rp3,dp3)                 #抛光修模矢高
        pxbj_var.set(round(rp3,3))
        pxkj_var.set(round(dp3,1))
        pxsg_var.set(round(hp3,2))
        if 透镜.r>0.0:
            rp4=-透镜.r        #抛光修模对修模半径和口径
            dp4=dm*k
            if dp4>math.fabs(rp4)*2:
                dp4=math.fabs(rp4)*2
        if 透镜.r<0.0:
            rp4=透镜.r
            dp4=dm*k
            if dp4>math.fabs(rp4)*2:
                dp4=math.fabs(rp4)*2
        hp4=计算矢高(rp4,dp4)   #抛光修模对修模矢高
        pxdbj_var.set(round(rp4,3))
        pxdkj_var.set(round(dp4,1))
        pxdsg_var.set(round(hp4,2))
        h=计算矢高(r,透镜.d)
        if 透镜.r>0.0:
            hc = h - 0.0125              #粗磨模矢高
            rc=-(hc**2+透镜.d**2/4)/(hc*2) 
        if 透镜.r<0.0:
            hc=h+0.0125
            rc=(hc**2+透镜.d**2/4)/(hc*2)    #粗磨模半径
        cmbj_var.set(round(rc,3))


    f1.pack_forget()
    f2.pack()
b1=tk.Button(f1,text='计算',command=计算)
b1.grid(row=6,column=1)

f2=tk.Frame(win)
tabControl=ttk.Notebook(f2)    
tab1 = ttk.Frame(tabControl)        
tabControl.add(tab1, text='基本参数')  
tab2 = ttk.Frame(tabControl)        
tabControl.add(tab2, text='精磨')  
tab3 = ttk.Frame(tabControl)        
tabControl.add(tab3, text='抛光')  
tab4 = ttk.Frame(tabControl)        
tabControl.add(tab4, text='抛修')  
tab5 = ttk.Frame(tabControl)        
tabControl.add(tab5, text='粗磨')  
tabControl.pack() 
#Tab1======
dr_l=tk.Label(tab1,text='D/R')
dr_l.grid(row=1,column=0)
dr_var=tk.StringVar()
dr_e=tk.Entry(tab1,show=None,textvariable=dr_var)
dr_e.grid(row=1,column=1)
qx_l=tk.Label(tab1,text='倾斜角')
qx_l.grid(row=2,column=0)
qx_var=tk.StringVar()
qx_e=tk.Entry(tab1,show=None,textvariable=qx_var)
qx_e.grid(row=2,column=1)
bd_l=tk.Label(tab1,text='摆动角')
bd_l.grid(row=3,column=0)
bd_var=tk.StringVar()
bd_e=tk.Entry(tab1,show=None,textvariable=bd_var)
bd_e.grid(row=3,column=1)
kj_l=tk.Label(tab1,text='球模口径')
kj_l.grid(row=4,column=0)
kj_var=tk.StringVar()
kj_e=tk.Entry(tab1,show=None,textvariable=kj_var)
kj_e.grid(row=4,column=1)
xs_l=tk.Label(tab1,text='摆动系数')
xs_l.grid(row=5,column=0)
xs_var=tk.StringVar()
xs_e=tk.Entry(tab1,show=None,textvariable=xs_var)
xs_e.grid(row=5,column=1)
#Tab1=======

#Tab2======
jjbj_l=tk.Label(tab2,text='精磨基模半径')
jjbj_l.grid(row=1,column=0)
jjbj_var=tk.StringVar()
jjbj_e=tk.Entry(tab2,show=None,textvariable=jjbj_var)
jjbj_e.grid(row=1,column=1)
jjkj_l=tk.Label(tab2,text='精磨基模口径')
jjkj_l.grid(row=2,column=0)
jjkj_var=tk.StringVar()
jjkj_e=tk.Entry(tab2,show=None,textvariable=jjkj_var)
jjkj_e.grid(row=2,column=1)
jjsg_l=tk.Label(tab2,text='精磨基模矢高')
jjsg_l.grid(row=3,column=0)
jjsg_var=tk.StringVar()
jjsg_e=tk.Entry(tab2,show=None,textvariable=jjsg_var)
jjsg_e.grid(row=3,column=1)

jxbj_l=tk.Label(tab2,text='精磨修模半径')
jxbj_l.grid(row=4,column=0)
jxbj_var=tk.StringVar()
jxbj_e=tk.Entry(tab2,show=None,textvariable=jxbj_var)
jxbj_e.grid(row=4,column=1)
jxkj_l=tk.Label(tab2,text='精磨修模口径')
jxkj_l.grid(row=5,column=0)
jxkj_var=tk.StringVar()
jxkj_e=tk.Entry(tab2,show=None,textvariable=jxkj_var)
jxkj_e.grid(row=5,column=1)
jxsg_l=tk.Label(tab2,text='精磨修模矢高')
jxsg_l.grid(row=6,column=0)
jxsg_var=tk.StringVar()
jxsg_e=tk.Entry(tab2,show=None,textvariable=jxsg_var)
jxsg_e.grid(row=6,column=1)
#Tab2====

#Tab3=====
pjbj_l=tk.Label(tab3,text='抛光基模半径')
pjbj_l.grid(row=1,column=0)
pjbj_var=tk.StringVar()
pjbj_e=tk.Entry(tab3,show=None,textvariable=pjbj_var)
pjbj_e.grid(row=1,column=1)
pjkj_l=tk.Label(tab3,text='抛光基模口径')
pjkj_l.grid(row=2,column=0)
pjkj_var=tk.StringVar()
pjkj_e=tk.Entry(tab3,show=None,textvariable=pjkj_var)
pjkj_e.grid(row=2,column=1)
pjsg_l=tk.Label(tab3,text='抛光基模矢高')
pjsg_l.grid(row=3,column=0)
pjsg_var=tk.StringVar()
pjsg_e=tk.Entry(tab3,show=None,textvariable=pjsg_var)
pjsg_e.grid(row=3,column=1)
fpjbj_l=tk.Label(tab3,text='返修抛光基模半径')
fpjbj_l.grid(row=4,column=0)
fpjbj_var=tk.StringVar()
fpjbj_e=tk.Entry(tab3,show=None,textvariable=fpjbj_var)
fpjbj_e.grid(row=4,column=1)
fpjkj_l=tk.Label(tab3,text='返修抛光基模口径')
fpjkj_l.grid(row=5,column=0)
fpjkj_var=tk.StringVar()
fpjkj_e=tk.Entry(tab3,show=None,textvariable=fpjkj_var)
fpjkj_e.grid(row=5,column=1)
fpjsg_l=tk.Label(tab3,text='返修抛光基模矢高')
fpjsg_l.grid(row=6,column=0)
fpjsg_var=tk.StringVar()
fpjsg_e=tk.Entry(tab3,show=None,textvariable=fpjsg_var)
fpjsg_e.grid(row=6,column=1)
#Tab3=========

#Tab4===============
pxbj_l=tk.Label(tab4,text='抛光修模半径')
pxbj_l.grid(row=1,column=0)
pxbj_var=tk.StringVar()
pxbj_e=tk.Entry(tab4,show=None,textvariable=pxbj_var)
pxbj_e.grid(row=1,column=1)
pxkj_l=tk.Label(tab4,text='抛光修模口径')
pxkj_l.grid(row=2,column=0)
pxkj_var=tk.StringVar()
pxkj_e=tk.Entry(tab4,show=None,textvariable=pxkj_var)
pxkj_e.grid(row=2,column=1)
pxsg_l=tk.Label(tab4,text='抛光修模矢高')
pxsg_l.grid(row=3,column=0)
pxsg_var=tk.StringVar()
pxsg_e=tk.Entry(tab4,show=None,textvariable=pxsg_var)
pxsg_e.grid(row=3,column=1)

pxdbj_l=tk.Label(tab4,text='抛光修模对修模半径')
pxdbj_l.grid(row=4,column=0)
pxdbj_var=tk.StringVar()
pxdbj_e=tk.Entry(tab4,show=None,textvariable=pxdbj_var)
pxdbj_e.grid(row=4,column=1)
pxdkj_l=tk.Label(tab4,text='抛光修模对修模口径')
pxdkj_l.grid(row=5,column=0)
pxdkj_var=tk.StringVar()
pxdkj_e=tk.Entry(tab4,show=None,textvariable=pxdkj_var)
pxdkj_e.grid(row=5,column=1)
pxdsg_l=tk.Label(tab4,text='抛光修模对修模矢高')
pxdsg_l.grid(row=6,column=0)
pxdsg_var=tk.StringVar()
pxdsg_e=tk.Entry(tab4,show=None,textvariable=pxdsg_var)
pxdsg_e.grid(row=6,column=1)
#Tab4============

#Tab5=============
cmbj_l=tk.Label(tab5,text='粗磨模半径')
cmbj_l.grid(row=1,column=0)
cmbj_var=tk.StringVar()
cmbj_e=tk.Entry(tab5,show=None,textvariable=cmbj_var)
cmbj_e.grid(row=1,column=1)
#Tab5=============

def f1_show():
    f2.pack_forget()
    f1.pack()
b2=tk.Button(f2,text='返回参数录入窗体',command=f1_show)
b2.pack()

win.mainloop()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sympy import *

#创建多项式
def f(x,y):
    return x**2+y**2

#梯度下降法
def gradient_descent(f):
    x,y=symbols('x y', real=True)
    dx=diff(f(x,y),x) #求梯度
    dy=diff(f(x,y),y)
    alpha=0.1 #学习率
    max_steps=1000 #最大迭代次数
    x0,y0=1,3 #初值
    f0=f(x0,y0) #计算初值代入时的函数值
    for i in range(1,max_steps):
        x1=x0-alpha*dx
        y1=y0-alpha*dy
        x1=x1.subs(x,x0) #symbol计算转换为数值计算
        y1=y1.subs(y,y0)
        f1=f(x1,y1)
        if (f0-f1)<10e-10: #设定停止迭代阈值
            break
        x0,y0,f0=x1,y1,f1 #更新
    return x1,y1,f1

x1,y1,f1=gradient_descent(f)
print(x1,y1,f1)
# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 16:08
# @FileName: 11.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com
'''

import numpy as np
import matplotlib.pyplot as plt
plt.subplot(2,1,1)
plt.plot([0,2,4,6,8],[3,1,4,5,2],'r--')
plt.ylabel('Grade')
plt.axis([-1,10,0,6])

plt.subplot(2,1,2)
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)
a=np.arange(0.0,5.0,0.02)
plt.ylabel('Change')
plt.plot(a,f(a),'g')

plt.show()
'''
import  pandas as pd
dt={'name':pd.Series(['Mayue','Llin','Euyun'],index=['0','1','2']),
    'pay':pd.Series([3000,4500,8000],index=['0','1','2'])}
salary=pd.DataFrame(dt,index=['0','1','2'])
print(salary)
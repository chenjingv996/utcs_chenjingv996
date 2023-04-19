#!/usr/bin/env python
#encoding:utf-8

import numpy as np

data=np.array([['name','age','gender'],
              ['aaa','25','female'],
              ['bbb','20','male'],
              ['ccc','28','female']])
filename='data.csv'
np.savetxt(filename,data,fmt='%s',delimiter=',')

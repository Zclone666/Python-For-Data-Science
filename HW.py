# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 21:22:48 2019

@author: cyril
"""

import numpy as ny
import pandas as ps
import datetime as dt
import random as rand
import math
#import tables
import textwrap


"""

    Задание №1


"""

authors=ps.DataFrame({'author_id':[1,2,3], 
'author_name':['Тургенев','Чехов','Островский']}, 
columns=['author_id','author_name']);
#_id', 'author_name']);

print(authors.loc[1,:]);

books=ps.DataFrame({'author_id':[1, 1, 1, 2, 2, 3, 3], '
book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо', 
'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 
'Таланты и поклонники'], 
'price':[450, 300, 350, 500, 450, 370, 290]}, 
columns=['author_id','book_title','price']);

#print(authors)





















"""

        Задание №2
#

#

#

#

#

#

#

#

#

#

#"""

#

#        Задание №2

#

#"""

#

#a_centred=a - ny.average(mean_a, axis=0)

#zx_=ny.array([[a.mean(axis=0),a.mean(axis=1)]])

#a_centred=ny.array([a[0] - mean_a_[0]])

#cntrd = ny.cov((ny.transpose(a[0])))

#{(vt - mean_a_[0+1*(vt%2)]) for vt in mean_a_ }

#a_centred= a-zx_

#print('a_centred = ', cntrd)

#

#print ('x = ', a[0][0], mean_a_[0])

#

#"""

#

#    Задание №3

#

#

#"""

#

#a_centred_sp=a_centred.dot(a_centred)/(ny.size(a)-1)

#

#print('Fin (a_centred_sp) = ', a_centred_sp)

#

#print('Test; selftest: ', (a.transpose())[0][1])

#ny.transpose(a)

#

#

#

#

#

#

#

#

#

#Задание №1

#

#

#"""

#

#a_=ny.array([[1, 2, 3, 3, 1], [6, 8, 11, 10, 7]])

#a_m=[1, 2, 3, 3, 1]

#b_m=[6, 8, 11, 10, 7]

#a=a_.transpose()

#a=ny.dstack((a_m,b_m))

#print

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
columns=['author_id','author_name'])

print(authors,'\n');

books=ps.DataFrame({'author_id':[1, 1, 1, 2, 2, 3, 3],
 'book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо',
 'Толстый и тонкий', 'Дама с собачкой', 'Гроза',
 'Таланты и поклонники'],
 'price':[450, 300, 350, 500, 450, 370, 290]}, 
columns=['author_id','book_title','price'])

print(books,'\n')

authors_price=ps.merge(authors, books, on='author_id', how='inner')

auth_p=authors_price.drop(['author_id','book_title'], axis=1)
print(authors_price,'\n')

top5=authors_price.nlargest(5, 'price')

print(top5,'\n')

authors_stat=ps.DataFrame({}, columns=['author_name'])
authors_stat=auth_p.groupby('author_name').agg(['min', 'max', 'mean'], axis=1, columns=['price'])      
authors_stat.rename({'min':'min_price', 'max':'max_price', 'mean':'mean_price'}, axis='columns', inplace=True)

print(authors_stat)

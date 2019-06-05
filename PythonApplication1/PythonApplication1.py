
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

books=ps.DataFrame({'author_id':[1, 1, 1, 2, 2, 3, 3],
 'book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо',
 'Толстый и тонкий', 'Дама с собачкой', 'Гроза',
 'Таланты и поклонники'],
 'price':[450, 300, 350, 500, 450, 370, 290]}, 
columns=['author_id','book_title','price']);

#print(authors)


authors_price=ps.merge(authors, books, on='author_id', how='inner')

top5=authors_price.nlargest(5, 'price')

print(top5)

author_s=ps.DataFrame({}, columns=['author_name'])
author_s=authors_price.groupby('author_name').agg(['min', 'max', 'mean'], axis=1, columns=['price'])       #{columns='price','min'})
author_s.rename({'min':'min_price', 'max':'max_price', 'mean':'mean_price'}, axis='columns', inplace=True)
print(author_s)
#print(author_s.loc[author_s['price']<5])
#author_s.drop(author_s.loc[author_s['min_price', 'max_price', 'mean_price']<5], axis=0)
#author_s.rename({'price':'min_price'}, axis='columns', inplace=True)
#print(author_s)
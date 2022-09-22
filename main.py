# -*- coding: utf-8 -*-
import pandas as pd;
import numpy as np;
import os;

df = pd.read_csv("./Toyota.csv")
car_data1 = pd.DataFrame(df)
missing = pd.DataFrame(df)

# whole data------------
print(car_data1)

# total no of indexes : 
print(car_data1.index);

# column names
print(car_data1.columns)

# 
print('axes')

print(car_data1.axes)

print("size : ")
print(car_data1.size)

print('ndim : ')
print(car_data1.ndim)


print('dtypes : ')
#  gives datatypes of all columns
print(car_data1.dtypes)

# accessing columns seperately

print('Accesing column name age : ')
print(car_data1.Age)

print('car info : ')
print(car_data1.info)
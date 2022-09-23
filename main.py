# -*- coding: utf-8 -*-
import pandas as pd;
import numpy as np;
import os;

df = pd.read_csv("./Toyota.csv")
car_data1 = pd.DataFrame(df)
# missing = pd.DataFrame(car_data1.row.isnull())

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

# info and describe 
# describe returns the stastical data of the csv read by the sys.

print('car info : ')
print(car_data1.info)

# accessing columns seperately

print('Accesing column name age : ')
print(car_data1.Age)

# Cleaning the data

car_data2 = pd.DataFrame(df)

# print(car_data2.Age.unique());

print(car_data2.MetColor.unique())

car_data2 =  car_data2.MetColor.replace(1.,1)
car_data2 = car_data2.Metcolor.replace(0.,0)

print(car_data2.MetColor.unique())

#car_data2 =  car_data2.Age.astype('int64')
#car_data2 =  car_data2.MetColor.astype('object')
#car_data2 =  car_data2.Automatic.astype('object')
#car_data2 =  car_data2.Doors.astype('int64')


# -*- coding: utf-8 -*-
import pandas as pd;
import numpy as np;
import os;

df = pd.read_csv("./Toyota.csv",index_col=0)


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

# making a deep copy to work on cleaning process

car_data2 = car_data1.copy(deep = True)

print(car_data2.info())

print(np.unique(car_data2['Age']))
print("unique in KM")
print(np.unique(car_data2['KM']))
print('unoque in Hp')
print(np.unique(car_data2['HP']))
print('unique values in col Doors')
print(np.unique(car_data2['Doors']))

#001 cleaned HP , KM

car_data2.replace(('????',"nan"),inplace=True)
car_data2.replace(('??','nan'),inplace=True)

# dtype 


# print to check
print(np.unique(car_data2['Age']))
print("unique values in KM : ")
print(np.unique(car_data2['KM']))
print('unique  values in Hp : ')
print(np.unique(car_data2['HP']))
print('unique values in col Doors : ')
print(np.unique(car_data2['Doors']))
print("np.unique values in automatic : " )
print(np.unique(car_data2['Automatic']))
print('unique values in Metcolor : ')
print(np.unique(car_data2['MetColor']))

# 003
# cleaning door col
car_data2.replace('five','5',inplace=True)
car_data2.replace('four','4',inplace=True)
car_data2.replace('three','3',inplace=True)


       # chnaging the dtypes to int64
car_data2['Doors'] = car_data2['Doors'].astype('int64')       


# print after cleaning 

print('after cleaning')
print(np.unique(car_data2['Doors']))
print('doors dtype after cleaning')
print(car_data2['Doors'].dtype)
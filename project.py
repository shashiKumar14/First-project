import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from flask import Flask

#1. Load Data
df=pd.read_csv("cruise_ship_info.csv")#reading of dataframe file by using recd csv ie., importing to current file by name df
print(df)

#2. Transformation
# - fix missing values
newData = df.dropna(axis = 0, how ='any')#droping of nan values rows with atleast one  value in that row
print("Number of rows with at least 1 NA value: ", (len(df)-len(newData)))
diff=(len(df)-len(newData))#finding difference of len(df) and len(newData)
if diff!=0:
    df.fillna(df.mean(), inplace=True)#filling of mean value in place of nan values
    print("Null values are replaced")
else:
    print("There is no Null value in this csv")

#- identify outliers (values which are beyond column standard deviation)
Q1 = df.quantile(0.25) #the datafrmae wich contain below 25 quantile
Q3 = df.quantile(0.75) #the datafrmae wich contain above 75 quantile
IQR = Q3 - Q1
lowerBound=Q1 - 1.5 * IQR  #lowerBound formula
upperBound=Q3 + 1.5 * IQR  #upperBound formula
print(lowerBound,upperBound)
IQRAllColumnData= df[((df < lowerBound) |(df > upperBound)).any(axis=1)] #the outliers in df which contains combindly
print(IQRAllColumnData)
tdWithBoolValues=(df< (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR)) #displaying bool values
print(tdWithBoolValues) #dataframe wich contain true value that is outlier
print(tdWithBoolValues.sum()) #count will be displayed how many outlier are present in each column

#- Normalize data
def norm():
    Normalization=df.iloc[:,2:]#reading of all columns and all rows except  1st and 2 columns because that contain string values
    for col in Normalization:
        mx=MinMaxScaler() #above the program imported MinMaxScaler from sklearn.preprocessing
        Normalization[col]=mx.fit_transform(Normalization[[col]]) #finding normalized data
        return Normalization
Normalization=norm()
print("Normalization",Normalization)

#4 .random splitting
randomsplitting_traindata = df.sample(frac=0.8,replace=False)      #In this  df.sample(frac=0.8) means 80% of the data selcted randomly and replace=False means once a row taken from the dataframe will not kept back into that dataframe
randomsplitting_testdata = df.drop(randomsplitting_traindata.index)   #In this droping of 80% of dataframe data and remaining 20% data will be displayed
print(randomsplitting_traindata)#output of randomsplitting_traindata will be displayed
print(randomsplitting_testdata)  #output of randomsplitting_testdata will be displayed

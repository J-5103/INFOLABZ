##--------PANDAS--------


import pandas as pd
import numpy as np

##---------------------Basic Operations------------------


#1. Create a Pandas Series from a Python list [10, 20, 30, 40, 50] and print its values.

a =[10,20,30,40,50]

my = pd.Series(a)
print(my)

#2. Create a Series from a dictionary: {'a': 100, 'b': 200, 'c': 300}.

dictionary={
    'a': 100,
    'b':200,
    'c':300
}

myvar=pd.Series(dictionary)
print(myvar)

#3.Convert a NumPy array [1.5, 2.5, 3.5, 4.5] into a Pandas Series.
arr=np.array([1.5,2.5,3.5,4.5])

myvar=pd.Series(arr)
print(myvar)

##------------Indexing & Selection--------------

#4.Access the third element of a Series

third=pd.Series(arr[2])
print(third)

#5.Retrieve all elements greater than 20 from a Series

greater_20=my[my>20]
print(greater_20)

#6. Select elements at index positions [0, 2, 4] from a given Series.
series=[0,2,4]

var=pd.Series(series,index=["day1","day2","day3"])
print(var)

##-----------------Mathematical Operations--------------

#7. Given a Series s = pd.Series([5, 10, 15, 20]), multiply each element by 2.

s=pd.Series([5,10,15,20])
multi=s*2
print(multi)

#8. Compute the mean, median, of a numerical Series.

num=[10,20,30,40,50,60,70,80,90,110]

mean=pd.Series(num).mean()
print(mean)

midean=pd.Series(num).median()
print(midean)

##--------------Filtering & Transformation----------

#10. Given a Series s = pd.Series([1, 2, 3, 4, 5, 6]), replace all even numbers with 0.

s=pd.Series([1,2,3,4,5,6],index=[1,2,3,4,5,6])
s[s%2==0]=0
print(s)

#11. Find the count of missing (NaN) values in a Series.

j=pd.Series([1,np.nan,2,np.nan,3,4,5,None])
missing_nan=j.isna().sum()
print(missing_nan)

#12. Replace all NaN values in a Series with the mean of the non-null values.

j=pd.Series([1,np.nan,2,np.nan,3,4,5,None])
mean_value=j.mean()
filled_j=j.fillna(mean_value)

print("original series:",j)
print("filled series with mean value:",filled_j)

##-----------------String Operations---------------

#13. Create a Series of string values [Laptop, keyboard', Mouse'] and convert all elements
#to uppercase.

string=pd.Series(["laptop","keyboard","mouse"])
Upper=string.str.upper()
print(Upper)

#14. Count the occurrences of the letter 'a' in each string in a Series.
occur=string.str.count("a")
print(occur)

##--------------------Sorting & Ranking---------------

#15. Sort a Series in ascending and descending order.

num=pd.Series([10,20,30,40,50,60,70,80,90,110])
asce=num.sort_values(ascending=True)
print(asce)

desce=num.sort_values(ascending=False)
print(desce)

#16. Rank the elements of a numerical Series.

num=pd.Series([10,20,30,40,50,60,70,80,90,110])
ranked=num.rank()
print(ranked)

##---------------------GroupBy & Value Counts----------------------

#19. Count the occurrence of each unique element in a Series

s=pd.Series([1,1,1,2,3,4,5,6,6,6,6,7,8,8,9,5,4,45,2,56])
value_unique=s.value_counts()##unique()
print(value_unique)

#20. Group a Series by values and calculate the sum for each unique value.
s=pd.Series([1,1,1,2,3,4,5,6,6,6,6,7,8,8,9,5,4,45,2,56])
group=s.groupby(s).sum()
print(group)
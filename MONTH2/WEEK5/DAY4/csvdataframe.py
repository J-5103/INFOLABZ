
import pandas as pd

df=pd.read_csv("Sales_Data.csv")

#----------------------------analyze data------------------------

#print columns
print(df.columns)

#print data
print(df)

#print first column name
print(df["TransactionID"])

#check null values
print(df.isnull().sum())

#check info of df
print(df.info())

#print rows and columns
print(df.shape)

#------------------handle null values---------------------
##1) drop
#
# df.dropna(inplace=True)
# print(df)

## 2) fill
#
# mean=df["Price"].mean()
# df["Price"].fillna(mean,inplace=True)
# print(df)

##------------------------operations----------------------

#print products name using unique
print("unique products:",df["Product"].unique())

# print count of products occur
print("products occurancy:",df["Product"].value_counts())

#print sum of price
print("sum of price:",df["Price"].sum())

#print average of price
print("average of price: ",df["Price"].mean())

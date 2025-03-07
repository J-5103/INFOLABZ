import  pandas as pd

data=[400,500,56,32,2]

df=pd.DataFrame(data)
print(df)

data2={
    "ahemdabad":[100,150,200],
    "area":[14,85,96],
    "age":[22,55,69]
}
df=pd.DataFrame(data2)
print(df)

print(df.columns)
print(df.shape)
print(df.loc[0])##agar index allocate kiya hoo to iloc use karna......yaa fir loc ke sath index dena padega


import pandas as pd

df_feedback=pd.read_csv("Feedback_Data.csv")
df_transaction=pd.read_csv("Transaction_Data.csv")
##----------------------------------------- Use Merge to Join-------------------------------
#1)Merge Both Dataset Data1 and Data2 according to their customer Id and save as final_customerdata.csv . use df.to_csv(“filename”) .
#
# df_merge=pd.merge(df_transaction,df_feedback,on="Customer_ID",how="inner")
# df_merge.to_csv("final_customerdata.csv",index=False)
# print("merged data save to final_customerdata.csv")

#2 ) print the total number of rows and columns(shape).
df=pd.read_csv("final_customerdata.csv")

df=pd.DataFrame(df)
print(df.shape)

#3 ) Print column names .
print(df.columns)

#4 ) check for the null values and handle with average of data ( if any).
print(df.isnull().sum())

###--------------------------------------------- Use concat to join.---------------------------------
#1 ) Add more customer data into final_customerdata.csv. Newdata.csv
#
# df_new=pd.read_csv("Newdata.csv")
#
# df_concat=pd.concat([df,df_new],ignore_index=True)
#
# df_concat.to_csv("final_data.csv",index=False)
# print("concated data save to final_data.csv")

df2=pd.read_csv("final_data.csv")

df2=pd.DataFrame(df2)
print(df2)
print(df2.isnull().sum())
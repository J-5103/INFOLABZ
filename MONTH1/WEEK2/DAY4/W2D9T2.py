import numpy as np

##statistical operation
##1) generate a 7*7 array
arr=np.random.randint(1,50,(7,7))
print(arr)

##2) find the mean ,median of the entire array
mean=np.mean(arr)
print("mean is:",mean)

median = np.median(arr)
print("median is:",median)

##3) find the column-wise mean and row-wise sum
col_mean = np.mean(arr,axis=0)
row_sum=np.sum(arr,axis=1)

print("colmn mean:",col_mean)
print("row sum:",row_sum)



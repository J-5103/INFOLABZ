import numpy as np
# np.random.seed(0)
# tempreture=np.random.uniform(-10,35,365)
# print(tempreture)
#
# #Find the hottest day, coldest day, and number of days above 30°C
#
# tempreture=np.sort(tempreture)[::-1 ]
# print("hottest day tempreture:",tempreture[0])
#
# print("coldest day tempreture:",tempreture[len(tempreture)-1])
#
# index = np.where(tempreture>30)
# print("numbers of days above 30 tempreture:",len(tempreture[index]))

##4. Airline Passenger Data Analysis
#a. Generate random monthly airline passenger numbers for 5 years

np.random.seed(0)
monthly_per_year=np.random.randint(50000,500000,(5,12))
#print(monthly_per_year)

#b. Find the month with the highest and lowest passengers.
max_passenger=np.max(monthly_per_year)
min_passenger=np.min(monthly_per_year)
print(max_passenger)

max_index=np.unravel_index(np.argmax(monthly_per_year),monthly_per_year.shape)
print(f"month with highest passenger:year:{max_index[0]+1},month:{max_index[1]+1}")

min_index=np.unravel_index(np.argmin(monthly_per_year),monthly_per_year.shape)
print(f"month with lowest passenger:year:{min_index[0]+1},month:{min_index[1]+1}")

#c. Calculate yearly average passengers and growth rate
yearly_avg=np.mean(monthly_per_year,axis=1)
print(yearly_avg)

growth_rate=np.diff(yearly_avg)/yearly_avg[:-1]*100
print(growth_rate)
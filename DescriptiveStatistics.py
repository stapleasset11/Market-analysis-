import numpy as np
import pandas as pd
data = [100,40,40,40,134,455,89,44,11,66,41,444,00,555]

#calculting mean
mean_ = np.mean(data)
print("Mean: ",mean_)
#calculting median
median_ = np.median(data)
print("Median: ",median_)
#calculating mode
from scipy import stats
mode_ = stats.mode(data)
print("Mode",mode_)
# calculating variance and standard deviation
variance_ = np.var(data)
std_ = np.std(data)

print("Variance: ",variance_)
print("Standard deviation: ",std_)


data_csv = pd.read_csv("percent-bachelors-degrees-women-usa.csv")

print(data_csv.drop(columns=['Year']).describe())

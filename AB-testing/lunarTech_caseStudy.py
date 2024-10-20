import pandas as pd
import os
import math
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm

file_path = os.path.expanduser("~/python-dataScience/AB-testing/ab_test_click_data.csv")
ab_test_df = pd.read_csv(file_path)

print(ab_test_df.head(50))
print(ab_test_df.describe())
print(ab_test_df.groupby("group").sum("click"))


# A simple barchat to give comprison btn no clicks and clicks in each group for better visual comprison.

palette = {0:"Red",1:"Green"}

plt.figure(figsize=(10,6))
ax = sns.countplot(x="group",hue="click",data=ab_test_df,palette=palette)
plt.title("Click Distribution in control and experimental groups.")
plt.xlabel("group")
plt.xlabel("Group")
plt.legend(title="click",labels=["No","Yes"])


group_counts = ab_test_df.groupby(["group"]).size()
group_click_counts = ab_test_df.groupby(["group","click"]).size().reset_index(name="count")

for x in ax.patches:
    height = x.get_height()
    group = 'exp' if x.get_x() < 0.5 else 'con'
    click = 1 if x.get_x() % 1 > 0.5 else 0

    total = group_counts.loc[group]
    percentage = (height / total) * 100


    ax.text(x.get_x() + x.get_width() / 2.,height + 5, f'{percentage:.1f}%',ha="center",color="black",fontsize=10)

    plt.tight_layout()
# plt.show()
plt.savefig('visualizations/click counts.png') 
plt.close()


#Model parameter for power analysis.

alpha = 0.05
print(f"The significsnce level is: {alpha}")

delta = 0.1 
print(f"Delta (minimum detectable defect):{delta}")

#Total number of clicks per group.

N_con = ab_test_df[ab_test_df["group"]=="con"].count().iloc[0]
N_exp = ab_test_df[ab_test_df["group"]=="exp"].count().iloc[0]

x_con = ab_test_df.groupby("group")["click"].sum().loc["con"]
x_exp = ab_test_df.groupby("group")["click"].sum().loc["exp"]

print(f"Number of clicks in control group: {x_con}")
print(f"Number of clicks in the experimental group: {x_exp}")

print("*************************************")
print(f"Sum of all clicks in controlled group: {N_con}")
print(f"Sum of clicks in the experimental group:{N_exp}")

#Calculating click probability.

p_con_hat = x_con/N_con
p_exp_hat = x_exp/N_exp

pooled_hat = (x_con + x_exp) / (N_con + N_exp)

print(f"Probability of clicks in control group:{p_con_hat}")
print(f"Probability of clicks in experimental group:{p_exp_hat}")
print(f"Pooled probability: {pooled_hat}")


#Calculating pooled variance.

pooled_variance = pooled_hat * (1-pooled_hat) * (1/N_con + 1/N_exp)
print(f"Pooled varince:{pooled_variance}")

#Calculating the test sttistics and standard error.

SE = np.sqrt(pooled_variance)
print(f"Standard error: {SE}")

Test_stat = (p_con_hat - p_exp_hat) / SE
print(f"Test statistics for the 2 sample Z-test: {Test_stat}")

z_crit = norm.ppf((1 - alpha)/2)
print(f"THe z-critical value from the stndrd normal distribution: {z_crit}")


#Calculating the p-value
p_value = 2 * (norm.sf(abs(Test_stat)))


"""
if p-value >= 0.05 it suggests strong evidence against the null hypothesis so we cn reject the null hypothesis

if p-value <= 0.05 it suggests weak evidence against the null hypothesis so we can go ahead and accept null hypothesis 
"""

print(f"P-value of the 2 sample Z-test: {p_value}")

# Determine the statistical significance.
def statistical_significance(p_value,alpha):

    
    if p_value < alpha:
        print("There is statistical significance,indicating that the observed differences between the groups are unlikely to have occured by accident")

    else:
        print("There is nostatistical significance indicating that the differences between the groups are likely to have occurred by accident.")


statistical_significance(p_value.any(),alpha)





 
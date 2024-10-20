import pandas as pd
data1 = pd.DataFrame({"key":["A","B","C","D","E","F","G"],
                      "value":[1,2,3,4,5,6,7]})


data2 = pd.DataFrame({"key":["C","D","E","F","G","H","I"],
                      "value":[8,9,10,11,12,13,14]})

print(data1)
print(data2)

merge_innerjoin = pd.merge(data1,data2, on="key",how="inner")
print(merge_innerjoin)  

merge_leftjoin = pd.merge(data1,data2, on="key",how="left")
print(merge_leftjoin)  

merge_rightjoin = pd.merge(data1,data2, on="key",how="right")
print(merge_rightjoin)  

merge_antiLeft = merge_left_anti = pd.merge(data1,data2, on="key",how="left",indicator=True)
print(merge_antiLeft)  


merge_antiRight = merge_right_anti = pd.merge(data1,data2, on="key",how="right",indicator=True)
print(merge_antiRight) 

merged_left = merge_antiLeft.drop("_merge",axis=1)
print(merged_left)

merged_right = merge_antiRight.drop("_merge",axis=1)
print(merged_right)
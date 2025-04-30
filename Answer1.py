import pandas as pd
import numpy as np

#-------------------------------------------------------------------------
data = pd.read_csv('./data/people.csv')

#-------------------------------------------------------------------------
average_age = data['Age'].mean()
median_age = data['Age'].median()
average_weight = data['Weight'].mean()
median_weight = data['Weight'].median()
print(f"Average Age: {average_age}")
print(f"Median Age: {median_age}")
print(f"Average Weight: {average_weight}")
print(f"Median Weight: {median_weight}")
print(100*"*")

# #-------------------------------------------------------------------------
mode_height = data['Height'].mode()[0]
mode_gender = data['Gender'].mode()[0]
mode_education = data['Education'].mode()[0]
print("Mode Height: ", mode_height)
print("Mode Gender: ", mode_gender)
print("Mode Education: ", mode_education)
print(100*"*")

# #-------------------------------------------------------------------------
age_range = data['Age'].max() - data['Age'].min()
height_range = data['Height'].max() - data['Height'].min()
weight_range = data['Weight'].max() - data['Weight'].min()
print("Age Range: ", age_range)
print("Height Range: ", height_range)
print("Weight Range: ", weight_range)
print(100*"*")

# #-------------------------------------------------------------------------
age_variance = np.var(data['Age'])
age_stddev = np.std(data['Age'])

height_variance = np.var(data['Height'])
height_stddev = np.std(data['Height'])

weight_variance = np.var(data['Weight'])
weight_stddev = np.std(data['Weight'])

print("Age Variance: ", age_variance)
print("Age Standard Deviation: ", age_stddev)
print("Height Variance: ", height_variance)
print("Height Standard Deviation: ", height_stddev)
print("Weight Variance: ", weight_variance)
print("Weight Standard Deviation: ", weight_stddev)
print(100*"*")

# #-------------------------------------------------------------------------
age_quartiles    = np.percentile(data['Age'],    [25, 50, 75])
height_quartiles = np.percentile(data['Height'], [25, 50, 75])
weight_quartiles = np.percentile(data['Weight'], [25, 50, 75])
print("Age Quartiles : ", age_quartiles)
print("Height Quartiles : ", height_quartiles)
print("Weight Quartiles : ", weight_quartiles)
print(100*"*")

# #-------------------------------------------------------------------------
age_quartiles = np.percentile(data['Age'], [25, 75])
age_iqr = age_quartiles[1] - age_quartiles[0]

height_quartiles = np.percentile(data['Height'], [25, 75])
height_iqr = height_quartiles[1] - height_quartiles[0]

weight_quartiles = np.percentile(data['Weight'], [25, 75])
weight_iqr = weight_quartiles[1] - weight_quartiles[0]

print("Age IQR: ", age_iqr)
print("Height IQR: ", height_iqr)
print("Weight IQR: ", weight_iqr)
print(100*"*")
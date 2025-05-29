from ucimlrepo import fetch_ucirepo
#imported from hw1
import numpy as np
import pandas as pd

from typing import List, Tuple
import matplotlib.pyplot as plt
import math

from sklearn.datasets import fetch_openml
from sklearn.neighbors import KNeighborsClassifier, NearestCentroid
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.inspection import DecisionBoundaryDisplay

  
# fetch dataset 
# diabetes_130_us_hospitals_for_years_1999_2008 = fetch_ucirepo(id=296) 
# print(type(diabetes_130_us_hospitals_for_years_1999_2008))
  
# # data (as pandas dataframes) 
# X = diabetes_130_us_hospitals_for_years_1999_2008.data.features 
# y = diabetes_130_us_hospitals_for_years_1999_2008.data.targets 
  
# metadata 
# print(diabetes_130_us_hospitals_for_years_1999_2008.metadata) 
  
# # variable information 
# print(diabetes_130_us_hospitals_for_years_1999_2008.variables) 


# load diabetic_data.csv
df = pd.read_csv('data/diabetic_data.csv')
# 101766 rows and 50 columns


# # print the first 5 rows of the dataframe
# print("First 5 rows of the dataframe:")
# print(df.head())
# # print the shape of the dataframe
# print("Shape of the dataframe:")
# print(df.shape)
# # print the columns of the dataframe
# print("Columns of the dataframe:")
# print(df.columns)
# # print the data types of the columns
# print("Data types of the columns:")
# print(df.dtypes)

# #print first 4 rows of payer_code feature
# print("First 4 rows of the payer_code feature:")
# print(df['payer_code'].head(4))

# creat subset of dataset with 50 collumns and 1000 rows

df_subset = df.iloc[:100, [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                            36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,49]]
# map admission_type_id, discharge_disposition_id, and admission_source_id to their corresponding values in data/IDS_mapping.csv
mapping_df = pd.read_csv('data/IDS_mapping.csv')
# Merge the mapping DataFrame with the subset DataFrame


# create mathplotlib figure and axis of df_subset as a scattered plot of age and gender, and color by diabetesMed
figure, axes = plt.subplots()

age_features = df_subset['age']
gender_features = df_subset['gender']
diabetes_med_features = df_subset['diabetesMed']

Diabetes_to_color = {'No': 'green', 'Yes': 'red'}
diabetes_color = diabetes_med_features.map(Diabetes_to_color)

axes.scatter(age_features, gender_features, c=diabetes_color)
axes.set_xlabel('Age')
axes.set_ylabel('Gender')
axes.set_title('Diabetes Medication Status by Age and Gender')

plt.show()
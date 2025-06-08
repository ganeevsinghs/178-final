# from ucimlrepo import fetch_ucirepo
import pandas as pd
  
# fetch dataset 
# diabetes_130_us_hospitals_for_years_1999_2008 = fetch_ucirepo(id=296) 
# print(type(diabetes_130_us_hospitals_for_years_1999_2008))
  

# load diabetic_data.csv
df = pd.read_csv('data/diabetic_data.csv')
# 101766 rows and 50 columns


'''
Pandas is a high-level data manipulation tool developed by Wes McKinney. 
It is built on the Numpy package and its key data structure is called the DataFrame. 
DataFrames allow you to store and manipulate tabular data in rows of observations and columns of variables.
'''
#There are several ways to create a DataFrame. 
#One way way is to use a dictionary.
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)

#changing index
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)

#Another way to create a DataFrame is by importing a csv file using Pandas.
# Import the cars.csv data: cars
try:
    cars = pd.read_csv('cars.csv')
    # Print out cars
    print(cars)
except Exception as er:
    print(er)

#Indexing DataFrames
#The single bracket with output a Pandas Series, while a double bracket will output a Pandas DataFrame.
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['cars_per_cap'])

# Print out country column as Pandas DataFrame
print(cars[['cars_per_cap']])

# Print out DataFrame with country and drives_right columns
print(cars[['cars_per_cap', 'country']])

#Square brackets can also be used to access observations (rows) from a DataFrame
# Import cars data
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out first 4 observations
print(cars[0:4])

# Print out fifth, sixth, and seventh observation
print(cars[4:6])

'''
You can also use loc and iloc to perform just about any data selection operation. 
loc is label-based, which means that you have to specify rows and columns based on 
their row and column labels. iloc is integer index based, so you have to specify rows 
and columns by their integer index like you did in the previous exercise.
'''
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])
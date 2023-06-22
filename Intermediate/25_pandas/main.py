import csv
import pandas as pd

with open('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        print(row)

df = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

# How many squirrel with different fur colors?
print(df.groupby('Primary Fur Color').size())

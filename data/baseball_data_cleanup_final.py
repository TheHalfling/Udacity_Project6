# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 19:20:48 2016

@author: Sherry
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 18:57:58 2016

@author: Sherry
"""
import csv
import pandas

datatable = []


f = open("Baseball_data_original.csv", 'rt')
try:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row['HR']) > 49:
            h = row['Handedness']
            if h == 'B':
                row['Handedness'] = 'Both'
            elif h == 'R':
                row['Handedness'] = 'Right'
            elif h == 'L':
                row['Handedness'] = 'Left'
            datatable.append(row)
finally:
    f.close()

#Create BMI Score for each player
for row in datatable:
    w = float(row['Weight'])
    h = float(row['Height'])
    row['BMI'] = 703*(w/(h*h))
    
    # Create BMI rating for each player
    if row['BMI'] <= 18.5:
        row['BMI Rating'] = "Underweight"
    elif row['BMI'] >= 30:
        row['BMI Rating'] = "Obese"
    elif row['BMI'] >= 25:
        row['BMI Rating'] = "Overweight"
    else:
        row['BMI Rating'] = "Healthy"
 
    
    

df = pandas.DataFrame(datatable)

df.to_csv('baseball_data_updated.csv', index=False)



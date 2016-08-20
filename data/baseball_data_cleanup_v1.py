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
            datatable.append(row)
finally:
    f.close()

df = pandas.DataFrame(datatable)

#df = df[df.HR >= 50]

#print df
    
#keys = df[0].keys()

df.to_csv('baseball_data_updated.csv', index=False)

"""
with open('Baseball_data_updated.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(df)"""

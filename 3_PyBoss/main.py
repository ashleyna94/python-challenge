# -*- coding: UTF-8 -*-
"""PyBoss

This script will convert the data into specific conversions.
It will: 
(1) split the name to 2 separate 'first name' and 'last
name' columns, 
(2) the date of birth will be re-written into dd/mm/yyyy
format,
(3) the SSN will be re-written so the first five numbers
are hidden, 
and (4) states will be re-written as two-letter abbreviations. 

Example:

  $ python main.py

"""



import csv

with open('old.csv', 'rb') as f:
    reader = csv.reader(f)
    newcsvdict = {"first name": [], "last name": []}
    for row in reader:
        first = row[0].split()[0]
        last = row[0].split()[1]
        newcsv["first name"].append(first)
        newcsv["last name"].append(last)

with open('new.csv', 'wb') as f:
    w = csv.DictWriter(f, newcsvdict.keys())
    w.writeheader()
    w.writerows(newcsvdict)
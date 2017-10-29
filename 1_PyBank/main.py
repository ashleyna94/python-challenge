# -*- coding: UTF-8 -*-
"""PyBank

This script will analyze the budget data and give a summary
table. 
It will include: 
(1) the total number of months included in the dataset, 
(2) the total amount of revenue gained over the entire period,
(3) the averange change in revenue between months over the
entire period, 
(4) the greatest increase in revenue (date and amount) over
the entire period, 
and (5) the greatest decrease in revenue (date and amount)
over the entire period. 

The summary table then will be exported as a text file.

Example:

  $ python main.py

"""

# Modules 
import os
import csv


# Import in the CSV file and create its path
csvpath = os.path.join("raw_data", "budget_data_1.csv")

dates = []
revenue = []
revenue_delta = []

# Open the CSV file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headers = next(csvreader)

    # Checking to make sure the CSV file is being read
    #for row in csvreader:
        #print(row)

    # 1. Count the months by counting the number of rows
    total_months = len(dates)
    #total_months = 0

    #for row in csvreader: 
        #total_months += 1

    # 2. Get the sum of the revenue
    # 3. Find the delta change b/w the revenues 
    previous_revenue = 0
    total_revenue = 0
    for row in csvreader:
        #print(row[1])
        revenue = int(row[1])
        total_revenue += revenue
        revenue_delta.append(revenue - previous_revenue)
        previous_revenue = revenue

    # 4. Find the greatest delta (max)
    # 5. Find the least amount of delta (min)
    #print(revenue_delta)
    sum_delta = sum(revenue_delta) 
    average_change = sum_delta / len(revenue_delta)
    
    dictionary = dict(zip(dates,revenue_delta))
    maximum = max(dictionary, key=dictionary.get)
    minimum = min(dictionary, key=dictionary.get)
    
    
    # Print the title of the summary table
    print("Financial Analysis")
    print("-" * 30)
    print(f"Total Months: {total_months}")
    print(f"Total Revenue: ${total_revenue}")
    print(f"Average Revenue Change: ${average_change}")
    print(f"Greatest Increase in Revenue: {maximum}, {dictionary[maximum]}")
    print(f"Greatest Decrease in Revenue: {minimum}, {dictionary[minimum]}")
"""
# Set variable for the output file
output_file = os.path.join("pybank_final.txt")

with open(output_file, "w") as text_file:
    text_file.write(
    print("Financial Analysis")
    print("-" * 30)
    print(f"Total Months: {total_months}")
    print(f"Total Revenue: ${total_revenue}")
    print(f"Average Revenue Change: ${average_change}")
    print(f"Greatest Increase in Revenue: {maximum}, {dictionary[maximum]}")
    print(f"Greatest Decrease in Revenue: {minimum}, {dictionary[minimum]}")
    )
    python main.py > pybank.txt
"""    

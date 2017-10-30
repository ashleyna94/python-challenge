# -*- coding: UTF-8 -*-
"""PyPoll

This script will analyze the poll data and give a summary 
table. 
It will include: 
(1) the total number of votes casted, 
(2) a complete list of candidates who received votes,
(3) the percentage of votes each candidate won, 
(4) the total number of votes each candidate won, 
and (5) the winner of the election based on popular vote. 

The summary table then will be exported as a text file.

Example:

  $ python main.py

"""
# Modules
import os
import csv
import collections


# Import in the CSV file and create its path
csvpath = os.path.join("raw_data", "election_data_2.csv")

voter_id = []
county = []
candidate = []

# Open the CSV file 
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headers = next(csvreader, None)

    names = collections.Counter() 

    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        
        # 2. Get a list of all candidates 
        # 4. Get the number of votes each candidate won 
        if row[2] not in candidate:
            candidate.append(row[2])
        names[row[2]] += 1

# 1. Get the total number of votes by counting rows 
total_votes = len(voter_id)

# 5. Calculate the winner (who received the most votes)
winner = max(names, default=0, key=names.get)

# 3. Get the ercentage of votes each candidate won 
# Print the summary table
print ("Election Results")
print("-" * 30)
print(f"Total Votes: {total_votes}")
print("-" * 30)
for key, value in names.items():
     print(key, ":", "%.2f" %((value/total_votes)*100),"(", value, ")")
print("-" * 30)
print(f"Winner: {winner}")
print("-" * 30)

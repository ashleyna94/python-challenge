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


# Import in the CSV file and create its path
csvpath = os.path.join("raw_data", "election_data_2.csv")

# Create a dictionary to hold the candidate info
candidates = {}

# Open the CSV file 
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # 1. Get the total number of votes 
    votes = list(csvreader)
    total_votes = len(votes)
    print(total_votes)

    """
    for row in csvreader:
        if row[2] not in candidates.keys():
            candidates[row[2]] = 0
        candidates[row[2]] = candidates[row[2]] + 1
    """

    """
    print("Election Results")
    print("-" * 30)
    print(f"Total Votes: {total_votes}")
    print("-" * 30)
    print(f"Khan: {}")
    print(f"Correy: {}")
    print(f"Li: {}")
    print(f"O'Tooley: {}")
    print("-" * 30)
    print(f"Winner: {}")
    print("-" * 30)
    """
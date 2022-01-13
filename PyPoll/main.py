# PyPoll Homework code

from asyncore import write
from gzip import WRITE
import os
import csv
import math


csvpath = os.path.join('PyPoll','Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    # csvreader below is an iterator and can only be used once until it must be used again. Either bring it down or collect all data iterating once
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    totalvotes = 0
    candidates = []
    votes = []
    candidate_votes = []

    for vote in csvreader:
        totalvotes = totalvotes + 1
        votes.append(vote[2])
        # Adds unique candidates to the list of candidates who received votes
        if vote[2] not in candidates:
            candidates.append(vote[2])
    # Counts votes for each candidate and creates a list of total votes each got
    for candidate in candidates:
        c = 0
        for vote in votes:
            if vote == candidate:
                c = c + 1
        candidate_votes.append(c)

    vote_percent = [round((votes/totalvotes),5) * 100 for votes in candidate_votes]
    #Creates a table by combining candidates, votes, and their percent total
    election_data = zip(candidates, candidate_votes, vote_percent)
    most_votes = max(candidate_votes)

# Creating output file and writing information from election data analysis
output_path = os.path.join("PyPoll", "analysis", "analysis.txt")

with open(output_path, 'w', newline='') as txtfile:
    
    txtfile.write("Election Results \n")
    txtfile.write("-------------------------- \n")
    txtfile.write(str(totalvotes) + "\n")
    txtfile.write("-------------------------- \n")
    for i in range(len(candidates)):
        txtfile.write(f"{candidates[i]}: {vote_percent[i]} ({candidate_votes[i]})")
        txtfile.write("\n")
    txtfile.write("-------------------------- \n")
    for result in election_data:
        if most_votes in result:
            txtfile.write(f"Winner: {result[0]}")
            txtfile.write("\n")       
    txtfile.write("-------------------------- \n")
    
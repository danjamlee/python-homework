import os
import csv

csvpath = "pypoll.csv"
txtpath = "poll.txt"

candidate = {}
canlist = []

with open(csvpath, newline = '') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    first_row = next(reader) 
    #Candidate list and voter count
    for row in reader:
        if row[2] in candidate: 
            candidate[row[2]] += 1
        else: 
            candidate[row[2]] = 1
    #total votes
    totalvote = sum(candidate.values())

    #winner
    winner = max(candidate, key=candidate.get)

print(
    f"\nElection Results\n"
    f"---------------------\n"
    f"Total Votes: {totalvote}\n"
    f"---------------------")
for k, v in candidate.items():
    print(f"{k} : {str(v)} Votes ({round((v/totalvote)*100, 3)}%)")
print(    
    f"---------------------\n"
    f"Winner: {winner}"
)

#print(finalized)

#with open("poll.txt", "w", newline="") as txt_file:
#    txt_file.write(finalized)


#import necessary items
import os
import csv

#bring in csv
pollcsv = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'election_data.csv')

#set up lists and values
total_votes = 0
candidate_column = []
candidates = []
candidate_votes = []
percent = []

#open csv and collect data
with open(pollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    Header = next(csvreader)
    #for loop to get number of votes and collect candidate info
    for row in csvreader:
        total_votes = total_votes + 1
        candidate_column.append(row[2])
    #second fore loop to get individual candidates (c), votes by candidate (v), and percent of total (t)
    for c in set(candidate_column):
        candidates.append(c)
        v = candidate_column.count(i)
        candidate_votes.append(v)
        t = (v/total_votes)*100
        percent.append(t)

#identify winning votes and winnter
winning_votes = max(candidate_votes)
winner = candidates[candidate_votes.index(winning_votes)]
    
#print to terminal
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(total_votes))    
for i in range(len(candidates)):
            print(candidates[i] + ": " + str(percent[i]) +"% (" + str(candidate_votes[i])+ ")")
print("The winner is: " + winner)

#print to txt file
with open('poll_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(total_votes) + "\n")
    for i in range(len(set(candidates))):
        text.write(candidates[i] + ": " + str(percent[i]) +"% (" + str(candidate_votes[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")
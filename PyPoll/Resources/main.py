import os
import csv
ElectionData =  os.path.join("election_data.csv")

#Variables
Candidates=[]
TotalVotes=0
PercentVotes =[]
NumberVotes=[]

with open(ElectionData, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

#Loop
    for row in csvreader:
        TotalVotes += 1

        if row[2] not in Candidates:
            Candidates.append(row[2])
            Index = Candidates.index(row[2])
            NumberVotes.append(1)
        else:
            Index = Candidates.index(row[2])
            NumberVotes[Index] += 1

#Perentage
    for Votes in NumberVotes:
        Percentage = (Votes/TotalVotes)*100
        Percentage = round(Percentage,3)
        Percentage = "%.3f%%" % Percentage
        
        PercentVotes.append(Percentage)

#Print Winner
    Winner = max(NumberVotes)
    Index = NumberVotes.index(Winner)
    WinningCandidate = Candidates[Index]

#Print Results
print("Election Results")
print("---------------------")
print(f"Total votes: {str(TotalVotes)}" )
print("---------------------")
#Candidates List 
for i in range(len(Candidates)):
    print(f"{Candidates[i]}: {str(PercentVotes[i])} ({str(NumberVotes[i])})")
print("---------------------")
print(f"Winner: {WinningCandidate}")
print("---------------------")

#Txt File Export
output = open("output.txt","w")
output.write("Election Results\n")
output.write("---------------------\n")
output.write(f"Total votes: {str(TotalVotes)}\n" )
output.write("---------------------\n")
#Candidates List
for i in range(len(Candidates)):
    output.write(f"{Candidates[i]}: {str(PercentVotes[i])} ({str(NumberVotes[i])})\n")
output.write("---------------------\n")
output.write(f"Winner: {WinningCandidate}\n")
output.write("---------------------\n")
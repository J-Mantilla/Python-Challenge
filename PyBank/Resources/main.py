import os
import csv

# Define the path to the CSV file
Election_Data_Path = os.path.join(os.getcwd(), "election_data.csv")

# Initialize variables
Total_Votes = 0
Candidates = {}
Winner = ""
Winner_Votes = 0

# Open and read the CSV file
with open(Election_Data_Path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Iterate through the data
    for Row in csvreader:
        # Count total votes
        Total_Votes += 1

        # Extract candidate name
        Candidate_Name = Row[2]

        # If candidate is already in the dictionary, increment vote count
        if Candidate_Name in Candidates:
            Candidates[Candidate_Name] += 1
        # Otherwise, add candidate to the dictionary with one vote
        else:
            Candidates[Candidate_Name] = 1

# Print election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {Total_Votes}")
print("-------------------------")

# Calculate and print the percentage of votes each candidate won
for Candidate, Votes in Candidates.items():
    Percentage = (Votes / Total_Votes) * 100
    print(f"{Candidate}: {Percentage:.3f}% ({Votes})")

    # Determine the winner
    if Votes > Winner_Votes:
        Winner = Candidate
        Winner_Votes = Votes

print("-------------------------")
print(f"Winner: {Winner}")
print("-------------------------")

# Write election results to an output file
with open("election_results.txt", "w") as output:
    output.write("Election Results\n")
    output.write("-------------------------\n")
    output.write(f"Total Votes: {Total_Votes}\n")
    output.write("-------------------------\n")

    for Candidate, Votes in Candidates.items():
        Percentage = (Votes / Total_Votes) * 100
        output.write(f"{Candidate}: {Percentage:.3f}% ({Votes})\n")

    output.write("-------------------------\n")
    output.write(f"Winner: {Winner}\n")
    output.write("-------------------------\n")
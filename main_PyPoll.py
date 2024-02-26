import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join('Resources', 'election_data.csv')

#initialize variables and create list for candidates
total_votes=0
candidates={}
winner_votes=0
Winner=""

# Define the function for count the data records
with open(election_csv,'r') as file:
    reader = csv.reader(file)
    header =next(reader)

    for row in reader: 
        #count the total votes
        total_votes=total_votes+1
        candidate_name=row[2]

        #if the candidate does not exit in the candidate list, add
        if candidate_name not in candidates:
            candidates[candidate_name]=0

            #add a vote to that candidate's count
        candidates[candidate_name]+=1

#Print the election results to the terminal with newlines for readability 

print("Election Results\n--------------------------\n") 
print(f"Total Votes :{int(total_votes)}\n")
print("--------------------------\n") 

#coalculate the percentage

for candidate in candidates: 
    #count the number of votes for each candidate
    votes = candidates[candidate]
    votes_percentage= (votes/total_votes)

    #print each candidate's vote
    print(f"{candidate}: {votes_percentage:.3%} ({votes})")

# find the winner 
    
    if votes > winner_votes:
        winner_votes=votes
        winner=candidate
        
print("--------------------------\n") 
print(f"Winner:{winner}\n")
print("--------------------------\n") 

# Set the path for the output file 
output_path = os.path.join("analysis", "election_results.txt") 
# Open the output file and write the analysis with newlines 
with open(output_path, "w") as txt_file: 
    txt_file.write("Election Results\n----------------------------\n") 
    txt_file.write(f"Total Votes :{int(total_votes)}\n") 
    txt_file.write("--------------------------\n")

    for candidate in candidates: 
    #count the number of votes for each candidate
        votes = candidates[candidate]
        votes_percentage= (votes/total_votes)
        txt_file.write(f"{candidate}: {votes_percentage:.3%} ({votes})\n")
    
    txt_file.write("--------------------------\n") 
    txt_file.write(f"Winner:{winner}\n")
    txt_file.write("--------------------------\n") 


#Import Libraries
import os
import csv

#Define variables
total_votes = 0
candidates = []
candidate_votes = []
percentage_votes = []
candidates_list = []
#Import csv file from Resources folder
election_data_csv = os.path.join("Resources", "election_data.csv")

with open(election_data_csv, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Set the first row to skip the headers
    first_row = next(csvreader)
    
    for row in csvreader:
        
        first_row = int(row[0])
        
        #Calculate total votes
        total_votes += 1
        
        #Create a list to track Candidates
        if row[2] not in candidates:
            candidates.append(row[2])
            
            #Create a list to track votes
            candidate_votes.append(1)
            
        else:
            
            #Assign an index to count votes
            candidates_index = candidates.index(row[2])
            
            #Add to vote count
            candidate_votes[candidates_index] += 1
            
    #Calculate percentages
    for votes in candidate_votes:
        percentage_votes.append((votes / total_votes) * 100)
        
        #Change votes to percent
    percent_1 = percentage_votes[0] 
    percent_1 = round(percent_1, 3)
    percent_2 = percentage_votes[1]
    percent_2 = round(percent_2, 3)
    percent_3 = percentage_votes[2]
    percent_3 = round(percent_3, 3)
    
    #combine lists into a dictionary
    
    candidate_dic = dict(zip(candidates, candidate_votes))
    winner = max(candidate_dic, key=lambda key: candidate_dic[key]) #cited from Stackoverflow
    
#Print data
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"{candidates[0]}: {percent_1}% ({candidate_votes[0]})")
print(f"{candidates[1]}: {percent_2}% ({candidate_votes[1]})")
print(f"{candidates[2]}: {percent_3}% ({candidate_votes[2]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#Write to textfile
output_path = os.path.join("analysis", "analysis.csv")

with open(output_path, 'w') as textfile:
    
    textfile.write("Election Results\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("-------------------------\n")
    textfile.write(f"{candidates[0]}: {percent_1}% ({candidate_votes[0]})\n")
    textfile.write(f"{candidates[1]}: {percent_2}% ({candidate_votes[1]})\n")
    textfile.write(f"{candidates[2]}: {percent_3}% ({candidate_votes[2]})\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write("-------------------------")

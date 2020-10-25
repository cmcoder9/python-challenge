#PyPoll
import os
import csv

election_data_csv = os.path.join('Resources','election_data.csv')

# Define the function and have it accept the 'election_data' as a parameter
def print_percentage(election_data):

# Header
            print("Election Results")
        
print('----------------------------------------------')  
#Read in the CSV file
with open(election_data_csv, newline="") as csv_file:
    
    # Split the data on the commas
    csv_reader = csv.reader(csv_file, delimiter=',')  
    csv_header = next(csv_reader)
    
    # Compile Candidate info
    # initialize a counter at 0
    vote_count = 0
    
     # initialize an empty list that is blank
    candidate_name_list = []
    candidate_name=""
    winner_name= ""
    votes_won=0
    total_number_of_votes=0
    
    for each_row in csv_reader:
        
        # The total number of votes cast included in the dataset
        # increase count for each row
        vote_count= vote_count + 1
    
        # A complete list of candidates who received votes
        candidate_name_list.append(str(each_row[2]))
        name_count ={}
      
    for name in candidate_name_list:
        if name in name_count:
            name_count[name] += 1
        else:
            name_count[name] = 1
        
        # The total number of votes each candidate won            
    print(name_count)

# The percentage of votes each candidate won
percentage_number_of_votes = (votes_won/total_number_of_votes) *100
        
print(f'Total Vote: {vote_count}')
        
print('----------------------------------------------')
        
print(f'Khan: {percentage_number_of_votes}, {votes_won}')
print(f'Correy: {percentage_number_of_votes}, {votes_won}')
print(f'Li: {percentage_number_of_votes}, {votes_won}')
print(f'OTooley: {percentage_number_of_votes}, {votes_won}')

print('----------------------------------------------')
#The winner of the election based on popular vote.
winner_name= max(name_count)
    
print(f'Winner: {winner_name}')
print('----------------------------------------------')


#PyPoll
import os
import csv

election_data.csv = os.path.join('Resources','election_data.csv')

# Define the function and have it accept the 'election_data' as a parameter
def print_percentage(election_data):
    
    # initialize a counter at 0
    vote_count = 0
    number_of_votes=0
    
     # initialize an empty list that is blank
    candidate_name_list = []
    
    
#Read in the CSV file
with open(election_data.csv, newline="") as csv_file:
    
    # Split the data on the commas
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    # Compile Candidate info
    name_to_check = input("Enter candidate name.")
    
    for row in csv_reader:
        
        # The total number of votes cast included in the dataset
        # increase count for each row
        vote_count = vote_count + 1

        # A complete list of candidates who received votes
        candidate_name = str(election_data[2])
    
        print(canditate_name)
        
        # The percentage of votes each candidate won


        # The total number of votes each candidate won


        #The winner of the election based on popular vote.

# Print out Elections Results: Canditate and their stats
print("Election Results")
print('----------------------------------------------')
print(f'Total Vote: {vote_count}')
print('----------------------------------------------')
print(f'Khan: {percent_number_of_votes}, {number_of_votes}')
print(f'Correy: {percent_number_of_votes}, {number_of_votes}')
print(f'Li: {percent_number_of_votes}, {number_of_votes}')
print(f'OTooley: {percent_number_of_votes}, {number_of_votes}')
print('----------------------------------------------')
print(f'Winner: {winner_name}')
print('----------------------------------------------')
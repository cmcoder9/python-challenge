import os
import csv

budget_data.csv = os.path.join('..', 'HW3_Resources', 'budget_data.csv' )

with open(budget_data.  
          csv) as csv_file:
    
    csv_reader = csv.reader(csv_file, delimiter= ',')
    
    print(csv_reader)

    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")
    
    for row in csv_reader:
        print(row)

# New Header
print("Financial Analysis")
print('----------------------------------------------')

#The total number of months included in the dataset


#The net total amount of "Profit/Losses" over the entire period


#The average of the changes in "Profit/Losses" over the entire period

#The greatest increase in profits (date and amount) over the entire period


#The greatest decrease in losses (date and amount) over the entire period
    
    
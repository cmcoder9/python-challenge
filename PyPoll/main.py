import os
import csv

budget_data_csv = os.path.join('..','PyBank', 'Resources', 'budget_data.csv')
# '../HW3_Resource...'
with open(budget_data_csv, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    print(csv_reader)

    csv_header = next(csv_reader)
    print(f'CSV Header:{csv_header}')

    # initialize a counter at 0
    month_count = 0
    net_total_amount = 0

    # initialize an empty list that is blank
    change_list = []
    previous_amount = 0
    total_change = 0
    average_change = 0
    date_list = []
    
    
    for each_row in csv_reader:

        # The total number of months included in the dataset
        # increase count for each row
        month_count = month_count + 1

        # The net total amount of "Profit/Losses" over the entire period
        # increase net_total_amount for each row
        net_total_amount = net_total_amount + int(each_row[1])
        
        # create a new list with changes
        change_list.append(int(each_row[1]) - previous_amount)
        previous_amount = int(each_row[1])
        
        # create a new list with Individual dates
        date_list.append(str(each_row[0]))
        
    for each_change in change_list[1:]:   
        total_change = total_change + each_change
        
      # Calculate the average of the changes in "Profit/Losses" over the entire period
        average_change = round(total_change/(month_count-1), 2)
       
    # zippesd 2 list, create a variable 
    date_change_list = [I for I in zip(date_list, change_list)]
    min_change = 0
    max_change = 0
    min_change_date = ''
    max_change_date = ''

    for each_change in date_change_list[:]:
        
        # The greatest increase in profits (date and amount) over the entire period
        if each_change[1]> max_change:
            max_change = each_change [1]
            
            max_change_date = each_change[0]
            
        # The greatest decrease in losses (date and amount) over the entire period
        if each_change[1] < min_change:
            min_change = each_change[1]
            min_change_date = each_change[0]
         
        
# # New Header
print("Financial Analysis")
print('----------------------------------------------')
print(f'Total Months: {month_count}')
print(f'Total: ${net_total_amount}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {max_change_date}, ${max_change}')
print(f'Greatest Decrease in Profits: {min_change_date}, ${min_change}')

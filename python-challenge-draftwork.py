import os
import csv

budget_data_csv = os.path.join('..', '..', 'HW3 Resources', 'budget_data.csv')
# '../HW3_Resource...'
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ',')
    
    print(csv_reader)


    csv_header = next(csv_reader)
    print(f'CSV Header: {csv_header}')
    
    # initialize a counter at 0
    month_count=0
    net_total_amount = 0
    # initialize an empty list that is blank
    change_list=[]
    previous_amount=0
    total_change=0
    min_change=0
    max_change=0
    for each_row in csv_reader:
        # increase count for each row
        month_count=month_count+1
        # month_count+=1
        
        # increase net_total_amount for each row
        net_total_amount=net_total_amount+int(each_row[1])
        
        # create a new list with changes
        change_list.append(int(each_row[1])-previous_amount)
        previous_amount=int(each_row[1])
        
    for each_change in change_list[1:]:
        total_change=total_change+each_change
        if each_change<min_change: 
            min_change=each_change
        if each_change>max_change:
            max_change=each_change
#         print(each_row)
    print(month_count)
    print(net_total_amount)
    print(total_change/month_count)
    print(change_list)
    print(min_change)
    print(max_change)

# # New Header
print("Financial Analysis")
print('----------------------------------------------')
print(f'Total Months: {month_count}')
print(f'Total Net Total Amount: {net_total_amount}')

#The total number of months included in the dataset


#The net total amount of "Profit/Losses" over the entire period


#The average of the changes in "Profit/Losses" over the entire period

#The greatest increase in profits (date and amount) over the entire period


#The greatest decrease in losses (date and amount) over the entire period
    
    
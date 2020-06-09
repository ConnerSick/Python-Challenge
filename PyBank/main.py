import os
import csv

csvpath = os.path.join("." , "budget_data.csv")
# define all variables
profit_sum = 0
months = 0
profit_change = 0
total_change = 0
largest_increase = 0
largest_decrease = 0
row_count = 0
profit = []
month_list = []
greatest_increase_month = 0
greatest_decrease_month = 0

with open(csvpath,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
# split csv values into 2 lists and count rows to determine number of months   
    for row in csvreader:
        profit.append(int(row[1]))
        month_list.append(row[0])
        profit_sum = profit_sum + (int(row[1]))
        row_count = row_count + 1        
        final_profit = row[1]
        
    print(f"Total months: {row_count}")
    print(f"Total: ${profit_sum}")   

# loop through lists to calculate changes between each month
    for x in range (0,row_count - 1):
        profit_change = int(profit[x+1]) - int(profit[x])
        total_change = total_change + profit_change
        
#         largest increase
        if (profit[x+1] - profit[x]) > largest_increase:
            largest_increase = (profit[x+1] - profit[x])
            greatest_increase_month = month_list[x+1]

#         Largest decrease 
        if (profit[x+1] - profit[x]) < largest_decrease:
            largest_decrease = (profit[x+1] - profit[x])
            greatest_decrease_month = month_list[x+1]
            
    print(f"Average Change: ${round(total_change/(row_count - 1),2)}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${largest_increase})") 
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${largest_decrease})") 
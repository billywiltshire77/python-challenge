# PyBank homework code
import os
import csv

csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(csv_header)

    distinct_months = []
    monthly_changes = []
    total = 0
    profit_loss = 0

    for row in csvreader:
        if row[0] not in distinct_months:
            distinct_months.append(row[0])
        total = total + int(row[1])
        monthly_change = int(row[1]) - profit_loss
        monthly_changes.append(monthly_change)
        profit_loss = int(row[1])
    
    combinded_list = zip(distinct_months, monthly_changes)
    average_change = sum(monthly_changes) / len(monthly_changes)
    greatest_increase = max(monthly_changes)
    greatest_decrease = min(monthly_changes)


    print("Financial Analysis")
    print("-------------------------------")
    print ("Total Months: " + str(len(distinct_months)))
    print ("Total: " + str(total))
    print("Average Change: " + str(average_change))

    for row in combinded_list:
        if greatest_increase in row:
            print(f"Greatest Increase: {row[0]} ({row[1]})")
        if greatest_decrease in row:
            print(f"Greatest Decrease: {row[0]} ({row[1]})")

import os
import csv

budget_dataCSV = os.path.join('../..', 'Instructions','PyBank','Resources', 'budget_data.csv')
output_path = os.path.join('../..', 'Instructions','PyBank','Output', 'output_pybank.csv')

total_months = []
total_profit = []
monthly_profit_change = []


with open(budget_dataCSV,newline="") as budget:
    csvreader = csv.reader(budget,delimiter=",")
    header = next(csvreader)
    for row in csvreader:

       total_months.append(row[0])
       total_profit.append(int(row[1]))
    for i in range(len(total_profit)-1):

       monthly_profit_change.append(total_profit[i+1]-total_profit[i])

max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1

with open(output_path, "w") as txt_file:
    #Print final results
    final_results =(f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {len(total_months)}\n"
        f"Total: ${sum(total_profit)}\n"
        f"Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}\n"
        f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})\n"
        f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})\n")
    print(final_results)

    # Save the results to the text file
    txt_file.write(final_results)  


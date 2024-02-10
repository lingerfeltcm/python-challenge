#import necessary items
import os
import csv
import statistics

#bring in csv
budgetcsv = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'budget_data.csv')
 
#set up lists and initiall values
profits = []
changes = []
month = []
 
total_months = 0
total = 0
total_change = 0
starting_profit = 0

# open csv and start collectin data
with open(budgetcsv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    #for loop to collect information
    for row in csvreader:    
      total_months = total_months + 1 
      month.append(row[0])
      profits.append(row[1])
      total = total + int(row[1])
      final_profit = int(row[1])
      monthly_change = final_profit - starting_profit
      changes.append(monthly_change)
      average_change = statistics.mean(changes)
      total_change = total_change + monthly_change
      starting_profit = final_profit
      greatest_increase = max(changes)
      greatest_decrease = min(changes)

      best_month = month[changes.index(greatest_increase)]
      worst_month = month[changes.index(greatest_decrease)]

#for some reason I am not getting the correct amount for the average, but I've not been able to figure that out.

#print to terminal
print("Financial Analysis")
print("Total Months: " + str(total_months))
print("Total Profits: " + "$" + str(total))
print("Average Change: " + "$" + str(int(average_change)))
print("Greatest Increase in Profits: " + str(best_month) + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(worst_month) + " ($" + str(greatest_decrease)+ ")")
print("----------------------------------------------------------")

#print to textfile
with open('budget_analysis.txt', 'w') as text:
    text.write("  Financial Analysis"+ "\n")
    text.write("    Total Months: " + str(total_months) + "\n")
    text.write("    Total Profits: " + "$" + str(total) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(best_month) + " ($" + str(greatest_increase) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(worst_month) + " ($" + str(greatest_decrease) + ")\n")
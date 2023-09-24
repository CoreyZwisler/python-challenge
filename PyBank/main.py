
#Import Libraries
import os
import csv

#Define Variables
total_months = 0
total_change = 0
average_change = 0
changes = 0
value = 0
greatest_increase = 0
greatest_decrease = 0
profits = []
dates = []

# Import the csv file from Recources folder
budget_data_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_data_csv, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')   
    
    #Set the first row to skip the headers
    first_row = next(csvreader)
    
    #Loop to find total number of months
    for row in csvreader:
        
        first_row = int(row[1])
        
        #Calculate the net total
        total_change += int(row[1])
        
        #Calculate changes and then average of those changes
        #Also keep track of dates
        if total_months == 0:
            value = first_row
        
        else: 
            changes = first_row - value
            profits.append(changes)
            dates.append(row[0])
            value = first_row
        
        #Calculate the total number of months
        total_months += 1 #Cited += to count from Stackoverflow
    
    # Calculate the average change rounded to 2 decimal places
    average_change = round(sum(profits) / len(profits), 2)
        
    #Calculate the Greatest Increase/Decrease
    greatest_increase = max(profits)
    greatest_decrease = min(profits)
    
    #Create index to assign dates to greatest increase/decrease
    greatest_inc_index = profits.index(greatest_increase)
    greatest_inc_date = dates[greatest_inc_index]
    
    greatest_dec_index = profits.index(greatest_decrease)
    greatest_dec_date = dates[greatest_dec_index]
    
    
#Print data       
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_change}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_inc_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_dec_date} (${greatest_decrease}) ")

#Write to a text file
output_path = os.path.join("analysis", "analysis.csv")

with open(output_path, 'w') as textfile:
    
    #Cited \n from geekstogeeks
    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${total_change}\n")
    textfile.write(f"Average Change: ${average_change}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_inc_date} (${greatest_increase})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_dec_date} (${greatest_decrease})")
    
    
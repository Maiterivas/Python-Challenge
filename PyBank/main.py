#PyBank Homework

#Import Python dependencies
import os
import csv

#CSV Budget Data file path
PyBankCSV = os.path.join('Resources', 'budget_data.csv')

#Name the output text file
output_file = os.path.join("PyBank.txt")

#Define variables to be used to make calculations
months = 0
net_profit = 0
current_profit = 0
starting_profit = 0
change_in_profits = 0
#Variable holding empty lists to be filled later with CSV data
profit_change = []
month = []

#Open CSV file
with open(PyBankCSV) as csvfile:
    #Specify how to read file into code
    csvreader = csv.reader(csvfile,delimiter=',')
#Skip over 1st row holding headers
    csvheader = next(csvreader)

#Calculate the total number of months included in the dataset(Read through each month)
    for row in csvreader:
        #Add month per row found
        months += 1
        #Use variable to define starting profit (1st row of data) and specify output type (integer)
        starting_profit = int(row[1])
        #Calculate net total amount of "Profit/Losses" over the entire period using loop
        net_profit += starting_profit

#Define what the first month will be to calculate changes in "Profit/Losses"
        if months == 1:
            current_profit = starting_profit
            #Make sure the loop continues to else after condition is met
            continue
#Calculate the changes in "Profit/Losses" over the entire period
        else:
            change_in_profits = starting_profit - current_profit
            #Store the result in the empty list created
            profit_change.append(change_in_profits)
            #Store the dates of each profit change in the other empty list
            month.append(row[0])
            #Reset the current profit for the next loop to run
            current_profit = starting_profit 

#Rounding average profit down to 2 decimals
avg_profit = round(sum(profit_change)/len(profit_change),2)

#Find greatest INcrease in profits (amount) over the entire period
greatest_increase = max(profit_change)
#Locate date of greatest increase with index function
highest_month = month[profit_change.index(greatest_increase)]

#Find greatest DEcrease in profits (amount) over the entire period
greatest_decrease = min(profit_change)
#Locate date of greatest increase with index function
lowest_month = month[profit_change.index(greatest_decrease)]

#Print the analysis in format provided from README to terminal:
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${net_profit}")
print(f"Average Change: ${avg_profit}")
print(f"Greatest Increase in Profits: {highest_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {lowest_month} (${greatest_decrease})")

#Name text file that will hold analysis results from terminal and specify relative path
PyBankAnalysis = 'Analysis/PyBank.txt'
#Open text file and make sure to specify 'w' write mode
with open(PyBankAnalysis, 'w', newline="") as output_file:
    #Write in text analysis to new file
    csvwriter = csv.writer(output_file)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Total Months: {months}"])
    csvwriter.writerow([f"Total: ${net_profit}"])
    csvwriter.writerow([f"Average Change: ${avg_profit}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {highest_month} (${greatest_increase})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {lowest_month} (${greatest_decrease})"])

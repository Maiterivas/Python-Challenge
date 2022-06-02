#PyPoll Homework

#Import Python dependencies
import os
import csv

#CSV Election Data file path
PyPollCSV = os.path.join('Resources', 'election_data.csv')

#Initialize variables to be used when looping through file
votes = 0
stockham_votes = 0
degette_votes = 0
doane_votes = 0
#Create an empty list that will hold all the candidates' names later
candidates_list = []
candidates = []

#Open CSV file
with open(PyPollCSV, 'r') as csvfile:
    #Specify how to read file into code
    csvreader = csv.reader(csvfile,delimiter=',')
    #Skip over 1st row holding headers
    csvheader = next(csvreader)

#Calculate the total number of votes included in the dataset
    for row in csvreader:
      votes += 1

      #Skip over the first 2 columns using (row[2])
      if row[2] == "Charles Casper Stockham":
        #Calculate total Stockham votes
        stockham_votes += 1
      #Calculate total DeGette votes
      elif row[2] == "Diana DeGette":
        degette_votes += 1
      #Calculate total Doane votes
      elif row[2] == "Raymon Anthony Doane":
        doane_votes += 1
#Populate a complete list of candidates who received votes
      candidates_list.append(row[2])
      
for candidate in candidates_list:
    if candidate not in candidates:
      candidates.append(candidate)

#Calculate percentage of votes for Stockham
stockham_percent = round((stockham_votes/votes)*100,3)
#Calculate percentage of votes for DeGette
degette_percent = round((degette_votes/votes)*100,3)
#Calculate percentage of votes for Doane
doane_percent = round((doane_votes/votes)*100,3)

#Find the winner of the election based on popular vote
if (stockham_percent > degette_percent) and (stockham_percent > doane_percent):
  #Printed candidates list using 'print(candidates)' to find index values by candidate
  winner = candidates[0]
elif (degette_percent > stockham_percent) and (degette_percent > doane_percent):
  winner = candidates[1]
elif (doane_percent > stockham_percent) and (doane_percent > degette_percent):
  winner = candidates[2]

#Print analysis to terminal with format provided by README file
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {votes}")
print(f"-------------------------")
print(f"Charles Casper Stockham: {stockham_percent}% ({stockham_votes})")
print(f"Diana DeGette: {degette_percent}% ({degette_votes})")
print(f"Raymon Anthony Doane: {doane_percent}% ({doane_votes})")
print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")

#Name text file that will hold analysis results from terminal and specify relative path
PyPollAnalysis = 'Analysis/PyPoll.txt'
#Export a text file with the results found above
with open(PyPollAnalysis, 'w', newline="") as output_file:
    #Write in text analysis to new file
    csvwriter = csv.writer(output_file)
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Total Votes: {votes}"])
    csvwriter.writerow([f"Charles Casper Stockham: {stockham_percent}% ({stockham_votes}"])
    csvwriter.writerow([f"Diana DeGette: {degette_percent}% ({degette_votes}"])
    csvwriter.writerow([f"Raymon Anthony Doane: {doane_percent}% ({doane_votes}"])
    csvwriter.writerow([f"-------------------------"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow([f"-------------------------"])